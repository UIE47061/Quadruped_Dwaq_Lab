# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
# Original code is licensed under BSD-3-Clause.
#
# Copyright (c) 2025-2026, The Legged Lab Project Developers.
# All rights reserved.
# Modifications are licensed under BSD-3-Clause.
#
# This file contains code derived from Isaac Lab Project (BSD-3-Clause license)
# with modifications by Legged Lab Project (BSD-3-Clause license).

"""
GO2 DWAQ Environment Configuration

DWAQ (Deep Variational Autoencoder for Walking) is a method that uses β-VAE to learn
latent representations from observation history for blind walking. This configuration
sets up the GO2 robot for DWAQ-based training.
"""

from isaaclab.managers import RewardTermCfg as RewTerm
from isaaclab.managers import SceneEntityCfg
from isaaclab.managers import EventTermCfg as EventTerm
from isaaclab.utils import configclass
from isaaclab.envs.mdp import events as isaaclab_events

from legged_lab.assets.unitree import GO2_CFG
from legged_lab.envs.base.base_env_config import (
    BaseAgentCfg,
    BaseEnvCfg,
    RewardCfg,
)
import legged_lab.mdp as mdp
from legged_lab.terrains import ROUGH_TERRAINS_CFG, DWAQ_HARD_TERRAINS_CFG


@configclass
class Go2DwaqRewardCfg(RewardCfg):
    """Reward configuration for GO2 DWAQ blind walking."""
    
    track_lin_vel_xy_exp = RewTerm(func=mdp.track_lin_vel_xy_yaw_frame_exp, weight=2.0, params={"std": 0.5})
    track_ang_vel_z_exp = RewTerm(func=mdp.track_ang_vel_z_world_exp, weight=2.0, params={"std": 0.5})
    lin_vel_z_l2 = RewTerm(func=mdp.lin_vel_z_l2, weight=-1.0)
    ang_vel_xy_l2 = RewTerm(func=mdp.ang_vel_xy_l2, weight=-0.05)
    energy = RewTerm(func=mdp.energy, weight=-1e-3)
    dof_acc_l2 = RewTerm(func=mdp.joint_acc_l2, weight=-2.5e-7)
    action_rate_l2 = RewTerm(func=mdp.action_rate_l2, weight=-0.01)
    
    undesired_contacts = RewTerm(
        func=mdp.undesired_contacts,
        weight=-1.0,
        params={"sensor_cfg": SceneEntityCfg("contact_sensor", body_names="(?!.*_foot).*"), "threshold": 1.0},
    )
    
    flat_orientation_l2 = RewTerm(func=mdp.flat_orientation_l2, weight=-1.0)
    termination_penalty = RewTerm(func=mdp.is_terminated, weight=-200.0)
    
    feet_air_time = RewTerm(
        func=mdp.feet_air_time,
        weight=0.15,
        params={"sensor_cfg": SceneEntityCfg("contact_sensor", body_names=".*_foot"), "threshold": 0.4},
    )
    
    feet_slide = RewTerm(
        func=mdp.feet_slide,
        weight=-0.25,
        params={
            "sensor_cfg": SceneEntityCfg("contact_sensor", body_names=".*_foot"),
            "asset_cfg": SceneEntityCfg("robot", body_names=".*_foot"),
        },
    )
    
    feet_force = RewTerm(
        func=mdp.body_force,
        weight=-3e-3,
        params={
            "sensor_cfg": SceneEntityCfg("contact_sensor", body_names=".*_foot"),
            "threshold": 500,
            "max_reward": 400,
        },
    )
    
    feet_stumble = RewTerm(
        func=mdp.feet_stumble,
        weight=-2.0,
        params={"sensor_cfg": SceneEntityCfg("contact_sensor", body_names=[".*_foot"])},
    )
    
    dof_pos_limits = RewTerm(func=mdp.joint_pos_limits, weight=-2.0)
    
    joint_deviation_hip = RewTerm(
        func=mdp.joint_deviation_l1_always,
        weight=-0.3,
        params={"asset_cfg": SceneEntityCfg("robot", joint_names=[".*_hip_joint"])},
    )
    
    # DWAQ Core Rewards
    alive = RewTerm(func=mdp.alive, weight=0.15)
    
    idle_penalty = RewTerm(
        func=mdp.idle_when_commanded,
        weight=-2.0,
        params={"cmd_threshold": 0.2, "vel_threshold": 0.1},
    )
    
    feet_swing_height = RewTerm(
        func=mdp.feet_swing_height,
        weight=-0.2,
        params={
            "sensor_cfg": SceneEntityCfg("contact_sensor", body_names=".*_foot"),
            "asset_cfg": SceneEntityCfg("robot", body_names=".*_foot"),
            "target_height": 0.08,
        },
    )


@configclass
class Go2DwaqEnvCfg(BaseEnvCfg):
    """GO2 DWAQ environment configuration for blind walking with VAE."""
    
    reward = Go2DwaqRewardCfg()

    def __post_init__(self):
        super().__post_init__()
        
        # Robot configuration
        self.scene.height_scanner.prim_body_name = "base"
        self.scene.robot = GO2_CFG
        self.scene.terrain_type = "generator"
        self.scene.terrain_generator = ROUGH_TERRAINS_CFG
        self.robot.terminate_contacts_body_names = ["base"]
        self.robot.feet_body_names = [".*_foot"]
        self.domain_rand.events.add_base_mass.params["asset_cfg"].body_names = ["base"]
        
        # Height scanner - asymmetric AC (actor is blind, critic has terrain info)
        self.scene.height_scanner.enable_height_scan = True
        self.scene.height_scanner.critic_only = True  # Actor is blind
        
        # Privileged information for Critic
        self.scene.privileged_info.enable_feet_info = True  # feet_pos + feet_vel (24 dim for 4 feet)
        self.scene.privileged_info.enable_feet_contact_force = True  # contact force (12 dim for 4 feet)
        self.scene.privileged_info.enable_root_height = True  # root height (1 dim)
        
        # DWAQ-specific: Observation history for VAE encoder
        self.robot.dwaq_obs_history_length = 5  # 5 frames of observation history
        
        # Standard history for AC
        self.robot.actor_obs_history_length = 1
        self.robot.critic_obs_history_length = 1
        
        # Gait phase configuration (disabled for basic quadruped DWAQ)
        self.robot.gait_phase.enable = False
        
        # Domain Randomization
        self.domain_rand.events.randomize_actuator_gains = EventTerm(
            func=isaaclab_events.randomize_actuator_gains,
            mode="startup",
            params={
                "asset_cfg": SceneEntityCfg("robot", joint_names=".*"),
                "stiffness_distribution_params": (0.8, 1.2),
                "damping_distribution_params": (0.8, 1.2),
                "operation": "scale",
                "distribution": "uniform",
            },
        )


@configclass  
class Go2DwaqAgentCfg(BaseAgentCfg):
    """GO2 DWAQ agent configuration."""
    experiment_name: str = "go2_dwaq"
    wandb_project: str = "go2_dwaq"
    runner_class_name: str = "DWAQOnPolicyRunner"

    def __post_init__(self):
        super().__post_init__()
        
        # Use ActorCritic_DWAQ policy with VAE encoder
        self.policy.class_name = "ActorCritic_DWAQ"
        self.policy.init_noise_std = 1.0
        self.policy.actor_hidden_dims = [512, 256, 128]
        self.policy.critic_hidden_dims = [512, 256, 128]
        
        # DWAQ encoder output dimension: velocity(3) + latent(16) = 19
        self.policy.cenet_out_dim = 19
        
        # Use DWAQPPO algorithm (PPO + autoencoder loss)
        self.algorithm.class_name = "DWAQPPO"
        self.algorithm.entropy_coef = 0.01
