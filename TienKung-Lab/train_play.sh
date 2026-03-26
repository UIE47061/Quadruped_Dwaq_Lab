python legged_lab/scripts/train.py --task=bigreddog_dwaq --headless --num_envs=4096 --max_iterations=10000
python legged_lab/scripts/play.py --task=bigreddog_dwaq --load_run=2026-03-25_23-32-07 --checkpoint=model_9999.pt

python legged_lab/scripts/train.py --task=little_white_dwaq --headless --num_envs=4096 --max_iterations=10000
python legged_lab/scripts/play.py --task=little_white_dwaq --load_run=2026-03-25_23-17-45 --checkpoint=model_9999.pt --terrain=flat


python legged_lab/scripts/train.py --task=go2_dwaq --num_envs=1 --max_iterations=10000
python legged_lab/scripts/train.py --task=bigreddog_dwaq --num_envs=1 --max_iterations=10000
python legged_lab/scripts/train.py --task=little_white_dwaq --num_envs=1 --max_iterations=10000

python legged_lab/scripts/play.py --task=go2_dwaq --load_run=2026-03-17_15-37-56




python legged_lab/scripts/sim2sim_little_white_dwaq.py --checkpoint /home/csl/Desktop/U1/G1DWAQ_Lab/TienKung-Lab/logs/little_white_dwaq/2026-03-19_11-04-42/model_2000.pt
python legged_lab/scripts/sim2sim_bigreddog_dwaq.py --checkpoint /home/csl/Desktop/U1/G1DWAQ_Lab/TienKung-Lab/logs/bigreddog_dwaq/2026-03-25_10-14-33/model_9999.pt