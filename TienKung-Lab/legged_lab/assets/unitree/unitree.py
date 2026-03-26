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


"""Configuration for Unitree robots.

The following configurations are available:

* :obj:`G1_MINIMAL_CFG`: G1 humanoid robot with minimal collision bodies

Reference: https://github.com/unitreerobotics/unitree_ros
"""

import isaaclab.sim as sim_utils
from isaaclab.actuators import DCMotorCfg, ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
from .utils import PaceDCMotorCfg


from legged_lab.assets import ISAAC_ASSET_DIR

GO2_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAAC_ASSET_DIR}/unitree/go2/go2.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=0
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.4),
        joint_pos={
            ".*L_hip_joint": 0.1,
            ".*R_hip_joint": -0.1,
            "F[L,R]_thigh_joint": 0.8,
            "R[L,R]_thigh_joint": 1.0,
            ".*_calf_joint": -1.5,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "base_legs": DCMotorCfg(
            joint_names_expr=[".*_hip_joint", ".*_thigh_joint", ".*_calf_joint"],
            effort_limit=23.5,
            saturation_effort=23.5,
            velocity_limit=30.0,
            stiffness=25.0,
            damping=0.5,
            friction=0.0,
        ),
    },
)
"""Configuration of Unitree Go2 using DC-Motor actuator model."""



# BIGREDDOG_CFG = ArticulationCfg(
#     spawn=sim_utils.UrdfFileCfg(
#         fix_base=False,
#         merge_fixed_joints=False,
#         replace_cylinders_with_capsules=False,
#         asset_path=f"{ISAAC_ASSET_DIR}/unitree/bigreddog/bigreddog.urdf",
#         activate_contact_sensors=True,
#         rigid_props=sim_utils.RigidBodyPropertiesCfg(
#             disable_gravity=False,
#             retain_accelerations=False,
#             linear_damping=0.0,
#             angular_damping=0.0,
#             max_linear_velocity=1000.0,
#             max_angular_velocity=1000.0,
#             max_depenetration_velocity=1.0,
#         ),
#         articulation_props=sim_utils.ArticulationRootPropertiesCfg(
#             enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=0
#         ),
#         joint_drive=sim_utils.UrdfConverterCfg.JointDriveCfg(
#             gains=sim_utils.UrdfConverterCfg.JointDriveCfg.PDGainsCfg(stiffness=0, damping=0)
#         ),
#     ),

#     init_state=ArticulationCfg.InitialStateCfg(
#         pos=(0.0, 0.0, 0.4),
#         joint_pos={
#             'FL_hip_joint': -0.1, # [rad]
#             'RL_hip_joint': 0.1, # [rad]
#             'FR_hip_joint': -0.1 , # [rad]
#             'RR_hip_joint': 0.1, # [rad]

#             'FL_thigh_joint': 0.8, # [rad]
#             'RL_thigh_joint': -0.8, # [rad]
#             'FR_thigh_joint': 0.8, # [rad]
#             'RR_thigh_joint': -0.8, # [rad]

#             'FL_calf_joint': -1.5, # [rad]
#             'RL_calf_joint': 1.5, # [rad]
#             'FR_calf_joint': -1.5, # [rad]
#             'RR_calf_joint': 1.5 # [rad]
#         },
#         joint_vel={".*": 0.0},
#     ),
#     soft_joint_pos_limit_factor=0.9,
#     actuators={
#         "base_legs": DCMotorCfg(
#             joint_names_expr=[".*_hip_joint", ".*_thigh_joint", ".*_calf_joint"],
#             effort_limit=23.5,
#             saturation_effort=23.5,
#             velocity_limit=30.0,
#             stiffness=25.0,
#             damping=0.5,
#             friction=0.0,
#         ),
#     },
# )
# """Configuration of Unitree Go2 using DC-Motor actuator model."""


Little_White_CFG = ArticulationCfg(
    spawn=sim_utils.UrdfFileCfg(
        fix_base=False,
        merge_fixed_joints=False,
        replace_cylinders_with_capsules=False,
        asset_path=f"{ISAAC_ASSET_DIR}/unitree/little_white/urdf/little_white.urdf",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=0
        ),
        joint_drive=sim_utils.UrdfConverterCfg.JointDriveCfg(
            gains=sim_utils.UrdfConverterCfg.JointDriveCfg.PDGainsCfg(stiffness=0, damping=0)
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.24),
        joint_pos={
            "FL_hip_joint": 0.1, "FL_thigh_joint": 0.5, "FL_calf_joint": -0.8,
            "FR_hip_joint": -0.1, "FR_thigh_joint": 0.5, "FR_calf_joint": -0.8,
            "RL_hip_joint": 0.1, "RL_thigh_joint": 0.8, "RL_calf_joint": -0.8,
            "RR_hip_joint": -0.1, "RR_thigh_joint": 0.8, "RR_calf_joint": -0.8
        }, 
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "base_legs": DCMotorCfg(
            joint_names_expr=[".*_hip_joint", ".*_thigh_joint", ".*_calf_joint"],
            effort_limit=23.5,
            saturation_effort=23.5,
            velocity_limit=30.0,
            stiffness=25.0,
            damping=0.5,
            friction=0.0,
        ),
    },
)
"""Configuration of Unitree Go2 using DC-Motor actuator model."""

BIGREDDOG_PACE_ACTUATOR_CFG = PaceDCMotorCfg(
    joint_names_expr=[".*_hip_joint", ".*_thigh_joint", ".*_calf_joint"],
    saturation_effort=23.5,
    effort_limit=23.5,
    velocity_limit=30.0,
    stiffness={".*": 25.0},  # P gain in Nm/rad
    damping={".*": 0.5},  # D gain in Nm s/rad
    
    encoder_bias=[0.0] * 12,  # calf, encoder bias in radians
    max_delay=2,  # max delay in simulation steps

    armature={"FR_hip_joint": 0.0520, "FR_thigh_joint": 0.0482, "FR_calf_joint": 0.0451,
            "FL_hip_joint": 0.0555, "FL_thigh_joint": 0.0477, "FL_calf_joint": 0.0488,
            "RR_hip_joint": 0.0557, "RR_thigh_joint": 0.0493, "RR_calf_joint": 0.0489,
            "RL_hip_joint": 0.0587, "RL_thigh_joint": 0.0488, "RL_calf_joint": 0.0493},

    viscous_friction={"FR_hip_joint": 0.2607, "FR_thigh_joint": 0.2736, "FR_calf_joint": 0.2292,
                    "FL_hip_joint": 0.1521, "FL_thigh_joint": 0.2204, "FL_calf_joint": 0.2424,
                    "RR_hip_joint": 0.2572, "RR_thigh_joint": 0.2638, "RR_calf_joint": 0.3440,
                    "RL_hip_joint": 0.2522, "RL_thigh_joint": 0.2357, "RL_calf_joint": 0.2909},
    )

BIGREDDOG_CFG = ArticulationCfg(
    spawn=sim_utils.UrdfFileCfg(
        fix_base=False,
        merge_fixed_joints=True,
        replace_cylinders_with_capsules=False,
        asset_path=f"{ISAAC_ASSET_DIR}/unitree/bigreddog/bigreddog.urdf",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=0
        ),
        joint_drive=sim_utils.UrdfConverterCfg.JointDriveCfg(
            gains=sim_utils.UrdfConverterCfg.JointDriveCfg.PDGainsCfg(stiffness=0, damping=0)
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.4),
        joint_pos={
            "FR_hip_joint": -0.0,
            "FL_hip_joint": 0.0,
            "RR_hip_joint": -0.0,
            "RL_hip_joint": 0.0,

            "FR_thigh_joint": 0.6,
            "FL_thigh_joint": 0.6,
            "RR_thigh_joint": -0.6,
            "RL_thigh_joint": -0.6,

            "FR_calf_joint": -1.0,
            "FL_calf_joint": -1.0,
            "RR_calf_joint":  1.0,
            "RL_calf_joint":  1.0,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "legs": BIGREDDOG_PACE_ACTUATOR_CFG,
    },
)
"""Configuration of Big reddog using DC motor.
"""