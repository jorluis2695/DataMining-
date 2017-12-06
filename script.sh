#!/bin/bash
paste soda_sa_n01_t1.txt soda_sl_n01_t1.txt soda_tp_n01_t1.txt soda_tx_n01_t1.txt soda_ty_n01_t1.txt soda_u_n01_t1.txt soda_v_n01_t1.txt soda_w_n01_t1.txt | cut -f 1-5,9,14,18,22,27,32,37 | sed -e 's/\s/,/g' | tr -s ',' > file1.txt
paste soda_sa_n01_t2.txt soda_sl_n01_t2.txt soda_tp_n01_t2.txt soda_tx_n01_t2.txt soda_ty_n01_t2.txt soda_u_n01_t2.txt soda_v_n01_t2.txt soda_w_n01_t2.txt | cut -f 1-5,9,14,18,22,27,32,37 | sed -e 's/\s/,/g' | tr -s ',' > file2.txt
paste soda_sa_n01_t3.txt soda_sl_n01_t3.txt soda_tp_n01_t3.txt soda_tx_n01_t3.txt soda_ty_n01_t3.txt soda_u_n01_t3.txt soda_v_n01_t3.txt soda_w_n01_t3.txt | cut -f 1-5,9,14,18,22,27,32,37 | sed -e 's/\s/,/g' | tr -s ',' > file3.txt
cat file1.txt file2.txt file3.txt > final.txt
