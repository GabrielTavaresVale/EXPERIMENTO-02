savimec 'create_dataset("art1:double","@/home/gabriel/Savime/examples/arquivo10-cosmo.bin");'



savimec 'create_tar("artigo2", "*", "implicit, tempo, int,0,73,1 |implicit, latitude, int,0,750,1 | implicit, longitude, int,0,710,1", "a,double");'


savimec 'load_subtar("artigo2", "ordered, tempo, 0,72 | ordered, latitude, 0,749 | ordered, longitude, 0, 709",  "a,art1");'


#__ Primeiro Exemplo



savimec 'subset(artigo2, latitude, 265, 265, longitude, 294,294);'


#__ Segundo  Exemplo
codigo=lat 371 long=392
savimec 'subset(artigo2, latitude, 370, 370, longitude, 392,392);'


#__ Terceiro  Exemplo
codigo= lat 447 long= 378

savimec 'subset(artigo2, latitude, 447, 447, longitude, 378,378);'


