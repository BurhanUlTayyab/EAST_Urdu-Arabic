export CUDA_VISIBLE_DEVICES=0
python multigpu_train.py --gpu_list=0 --input_size=256 --batch_size_per_gpu=7 --checkpoint_path=/home/burhan/EAST/modelse --text_scale=512 --training_data_path=/home/burhan/data/ --geometry=RBOX --learning_rate=0.0001 --num_readers=24 --pretrained_model_path=resnet_v1_50.ckpt

