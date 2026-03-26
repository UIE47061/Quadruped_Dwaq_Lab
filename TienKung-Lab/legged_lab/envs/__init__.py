# Copyright (c) 2021-2024, The RSL-RL Project Developers.
# All rights reserved.
# Original code is licensed under the BSD-3-Clause license.
#
# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# Copyright (c) 2025-2026, The Legged Lab Project Developers.
# All rights reserved.
#
# Copyright (c) 2025-2026, The TienKung-Lab Project Developers.
# All rights reserved.
# Modifications are licensed under the BSD-3-Clause license.
#
# This file contains code derived from the RSL-RL, Isaac Lab, and Legged Lab Projects,
# with additional modifications by the TienKung-Lab Project,
# and is distributed under the BSD-3-Clause license.

from legged_lab.envs.base.base_env import BaseEnv
from legged_lab.envs.base.base_env_config import BaseAgentCfg, BaseEnvCfg

from legged_lab.envs.go2.go2_dwaq_env import Go2DwaqEnv
from legged_lab.envs.go2.go2_dwaq_config import (
    Go2DwaqAgentCfg,
    Go2DwaqEnvCfg,
)

from legged_lab.envs.bigreddog.bigreddog_dwaq_env import BigRedDogDwaqEnv
from legged_lab.envs.bigreddog.bigreddog_dwaq_config import(
    BigRedDogDwaqAgentCfg,
    BigRedDogDwaqEnvCfg
)

from legged_lab.envs.little_white.little_white_dwaq_env import LittleWhiteDwaqEnv
from legged_lab.envs.little_white.little_white_dwaq_config import (
    LittleWhiteDwaqAgentCfg,
    LittleWhiteDwaqEnvCfg,
)

from legged_lab.utils.task_registry import task_registry


task_registry.register("go2_dwaq", Go2DwaqEnv, Go2DwaqEnvCfg(), Go2DwaqAgentCfg())

task_registry.register("bigreddog_dwaq", BigRedDogDwaqEnv, BigRedDogDwaqEnvCfg(), BigRedDogDwaqAgentCfg())
task_registry.register("little_white_dwaq", LittleWhiteDwaqEnv, LittleWhiteDwaqEnvCfg(), LittleWhiteDwaqAgentCfg())