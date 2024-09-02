from typing import Callable, Optional
import torch
from torch import nn
from torch import Tensor
import torch.nn.functional as F
import numpy as np
import math
import pdb
from layers.SVQ_backbone import SVQ_backbone
from layers.SVQ_layers import series_decomp
from layers.sparselinear import SparseLinear

class Model(nn.Module):
    def __init__(self, configs, max_seq_len:Optional[int]=1024, d_k:Optional[int]=None, d_v:Optional[int]=None, norm:str='BatchNorm', attn_dropout:float=0., 
                 act:str="gelu", key_padding_mask:bool='auto',padding_var:Optional[int]=None, attn_mask:Optional[Tensor]=None, res_attention:bool=True, 
                 pre_norm:bool=False, store_attn:bool=False, pe:str='zeros', learn_pe:bool=True, pretrain_head:bool=False, head_type = 'flatten', verbose:bool=False, **kwargs):
        
        super().__init__()
        
        # load parameters
        c_in = configs.enc_in
        self.enc_in = configs.enc_in
        context_window = configs.seq_len
        target_window = configs.pred_len
        n_layers = configs.e_layers
        n_heads = configs.n_heads
        d_model = configs.d_model
        d_ff = configs.d_ff
        dropout = configs.dropout
        fc_dropout = configs.fc_dropout
        head_dropout = configs.head_dropout
        individual = configs.individual
        sout = configs.sout
    
        patch_len = configs.patch_len
        stride = configs.stride
        padding_patch = configs.padding_patch
        
        revin = configs.revin
        affine = configs.affine
        subtract_last = configs.subtract_last
        

        kernel_size = configs.kernel_size
        
                     
        codebook_size = configs.codebook_size
        wFFN = configs.wFFN
        svq = configs.svq
        length = configs.length

        num_quantizers = configs.num_quantizers
        groups = configs.groups


        self.model = SVQ_backbone(codebook_size, length, svq=svq, wFFN=wFFN, c_in=c_in, context_window = context_window, target_window=target_window, patch_len=patch_len, stride=stride,
                                  num_quantizers=num_quantizers, groups=groups, max_seq_len=max_seq_len, n_layers=n_layers, d_model=d_model,
                                  n_heads=n_heads, d_k=d_k, d_v=d_v, d_ff=d_ff, norm=norm, attn_dropout=attn_dropout,
                                  dropout=dropout, act=act, key_padding_mask=key_padding_mask, padding_var=padding_var, 
                                  attn_mask=attn_mask, res_attention=res_attention, pre_norm=pre_norm, store_attn=store_attn,
                                  pe=pe, learn_pe=learn_pe, fc_dropout=fc_dropout, head_dropout=head_dropout, padding_patch = padding_patch,
                                  pretrain_head=pretrain_head, head_type=head_type, individual=individual, sout =sout, revin=revin, affine=affine,
                                  subtract_last=subtract_last, verbose=verbose, **kwargs)


    def forward(self, x):
        x = x.permute(0,2,1)
        x, loss = self.model(x)
        x = x.permute(0,2,1)    # x: [Batch, Input length, Channel]
        return x, loss
