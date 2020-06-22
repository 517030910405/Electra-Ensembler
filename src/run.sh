export GLUE_DIR=/path/to/glue
export TASK_NAME=MRPC
# rm -r cache_dir
TASK_NAME="CoLA"
python3 run_glue2.py \
    --model_name_or_path "google/electra-large-discriminator" \
    --task_name CoLA \
    --do_train \
    --do_eval \
    --do_predict \
    --data_dir $TASK_NAME \
    --max_seq_length 128 \
    --per_device_eval_batch_size=32   \
    --per_device_train_batch_size=32   \
    --learning_rate 1e-5 \
    --max_steps 374 \
    --warmup_steps 320 \
    --cache_dir cache_dir \
    --overwrite_output_dir \
    --evaluate_during_training \
    --logging_dir log_dir \
    --logging_steps 34 \
    --logging_first_step \
    --output_dir output/$TASK_NAME/
    # --num_train_epochs 2.0 \
    # --warmup_steps \ 