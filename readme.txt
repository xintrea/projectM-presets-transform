Можно изменять:

comp_1=`sampler sampler_rose;
warp_1=`sampler sampler_lichen;
comp_1=`sampler sampler_fc_sunrise; - здесь sunrise - имя файла
comp_1=`sampler sampler_fw_sky; - здесь sky - имя файла
comp_1=`sampler sampler_grad = sampler_state { - сложная обработка grad - есть файл, 
                                                 sampler_state - это функция
warp_1=`sampler sampler_fw_clouds; - здесь clouds - имя файла                                                 
                                           

Не трогать:
comp_1=`sampler sampler_rand00; - и так случайный
warp_1=`sampler sampler_rand01; - и так случайный
warp_2=`sampler sampler_pw_noise_lq;
warp_1=`sampler sampler_rand00_smalltiled; - подумать, может менять можно


Префиксы:

sampler_fw_main - не менять
sampler_fc_main
sampler_pw_main
sampler_pc_main


sampler_fw_ - не менять если имя файла входит в внутреннее имя
sampler_fc_
sampler_pw_
sampler_pc_

Внутреннее имя:

noise_lq       
noise_lq_lite  
noise_mq       
noise_hq       
noisevol_lq    
noisevol_hq    


Зависимые имена (изменять в паре):
        
comp_2=`sampler sampler_clouds2;
comp_3=`float4 texsize_clouds2;

sampler sampler_rand07;
float4  texsize_rand07;
shader_body 
{    
 ...
 float3 color = tex2D(sampler_rand07, uv);
 ...
}



