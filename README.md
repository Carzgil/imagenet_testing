# nyu-cloudml-2023-fall-prj1-helper

1. Please check the *README* file for file explanation and steps
2. For detailed steps please refer to the `*_help.pdf`
3. Some changes for Spring 2024 corresponds to the `*_help.pdf`

## Changes
1. use `sinfo` to get the name of the 'partitions' in the `burst` environment.
   1. `squeue` to find jobs in the account
   2. `scancel <jobid>` to kill your own job.
   3. what is JOB: 'srun' command starts an interactive job.
3. change account to `--account=csci_ga_3033_085-20234sp`
4. if `python ...` not work as expected, replace with `python3 ...`
5. A100 runs use mixed-data type, many computations turned into fp16, must find the fp16 counter event. One example is: `smsp__sass_thread_inst_executed_op_fp16_pred_on`.
   1. To find more on counters, either checkout the docu: https://docs.nvidia.com/nsight-compute/NsightComputeCli/index.html
   2. Or use NCU command: `<to be added>`
