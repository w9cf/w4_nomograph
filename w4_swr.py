from pynomo.nomographer import Nomographer
from math import log
from pyx import text
 
F_params={
   'u_min':10.0,
   'u_max':2000.0,
   'function':lambda u:log(u),
   'title':'Forward',
   'scale_type':'log smart',
   'tick_side':'left',
   'tick_text_levels': 3,
   'tick_levels': 4,
   'text_size_0':text.size.large,
   'text_size_1':text.size.small,
   'text_size_2':text.size.scriptsize,
   'title_x_shift':-0.5,
}

R_params={
   'u_min':100.0,
   'u_max':1.0,
   'function':lambda u:-log(10*u),
   'title':'Reverse',
   'scale_type':'log smart',
   'tick_side':'right',
   'tick_text_levels': 2,
   'tick_levels': 4,
   'text_size_0':text.size.large,
   'text_size_1':text.size.small,
   'text_size_2':text.size.scriptsize,
   'title_x_shift':0.5,
}

S_params={
   'tag':'swr',
   'u_min':1.05,
   'u_max':1.0e6,
   'function':lambda u:(2.*log((u-1)/(u+1))+log(100.0/10.0)),
   'title':'SWR',
   'title_x_shift':0.5,
   'scale_type':'manual line',
   'manual_axis_data':{1.05:'1.05',1.06:'',1.07:'',1.08:'',1.09:'',
      1.1:'1.1',1.12:'',1.14:'',1.16:'',1.18:'',1.2:'1.2',1.25:'',
      1.3:'1.3',1.35:'',1.4:'1.4',1.5:'1.5',1.6:'',1.7:'',1.8:'',
      1.9:'',2.0:'2.0',2.5:'',3.0:'3.0',4.0:'4.0',5.0:'',6.0:'6.0',
      8.0:'',10.0:'10',1.0e6:r'$\infty$',
   },
   'tick_side':'right',
   'tick_text_levels': 3,
   'tick_levels': 3,
}


Rl_params={
   'tag':'swr',
   'u_min':30.0,
   'u_max':1.0e-6,
   'function':lambda u:-u*log(10.0)/10.0+log(100.0/10.0),
   'align_func':lambda u:(1+10.0**(-u/20.0))/(1.0-10**(-u/20.0)),
   'title':'Return Loss (dB)',
   'tick_text_levels': 2,
   'tick_levels': 2,
   'title_x_shift':-1.5,
}
 
block_params={
   'block_type':'type_1',
   'f1_params':F_params,
   'f2_params':S_params,
   'f3_params':R_params,
   'width':5.0,
   'height':15.0,
}

block_rl_params={
   'block_type':'type_8',
   'f_params':Rl_params,
}
 
main_params={
   'filename':'w4_swr_nomograph.pdf',
   'paper_height':15.0,
   'paper_width':8.0,
   'block_params':[block_params,block_rl_params],
   'transformations':[('scale paper',),('polygon',)]
}
 
Nomographer(main_params)

