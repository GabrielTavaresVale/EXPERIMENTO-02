savimec 'create_dataset("dschuvatotal:double","@/home/gabriel/Savime/examples/precipitacao-Total-cosmo.bin");'


savimec 'create_dataset("dslatitude:double","@/home/gabriel/Savime/examples/lat-transladada-cosmo.bin");'




savimec 'create_dataset("dslongitude:double","@/home/gabriel/Savime/examples/long-transladada-cosmo.bin");'

savimec 'create_dataset("dstempo:double","@/home/gabriel/Savime/examples/indice-tempo-total-cosmo.bin");'




savimec 'create_tar("cosmoArtigo47", "*", "explicit, tempo,dstempo|explicit,latitude,dslatitude |explicit,longitude,dslongitude", "chuva,double");'

savimec 'create_dataset("dscoor:long", "0:1:47497002:1");'
savimec 'create_dataset("dscoor10:long", "0:1:10:1");'
savimec 'create_dataset("dscoor100:long", "0:1:100:1");'
savimec 'create_dataset("dscoor1000:long", "0:1:1000:1");'
savimec 'create_dataset("dscoor10000:long", "0:1:10000:1");'
savimec 'create_dataset("dscoor100000:long", "0:1:100000:1");'
savimec 'create_dataset("dscoorm:long", "0:1:1000000:1");'
savimec 'create_dataset("dscoor:long", "0:1:10000000:1");'




savimec 'create_dataset("dscoor7:long", "0:1:47000000:1");'




savimec 'load_subtar("cosmoArtigo", " total, tempo, 0, 47497001, dscoor1000000 |total, latitude, 0 ,47497001, dscoor1000000| total, longitude, 0, 47497001, dscoor1000000",  "chuva,dschuvatotal");'



savimec 'load_subtar("cosmoArtigo2", " total, tempo, 0, 10, dscoor10 |total, latitude, 0 ,10, dscoor10| total, longitude, 0, 10, dscoor10",  "chuva,dschuvatotal");'


savimec 'load_subtar("cosmoArtigo47", " total, tempo, 0, 47000000, dscoor47 |total, latitude, 0 ,47000000, dscoor47| total, longitude, 0, 47000000, dscoor47",  "chuva,dschuvatotal");'



savimec 'select(cosmoArtigo)'


savimec 'where(cosmoArtigo,  latitude= 34.0700 and longitude >40.3000);'




------------------- Primeiro Exemplo
savimec 'where(cosmoArtigo,  latitude= 26.545 and longitude >29.498);'




savimec 'subset(cosmoArtigo,tempo,2001102100.0000,2001102200.0000, latitude, 34.0700,34.0700, longitude, 40.3000,40.3000);'


savimec 'subset(cosmoArtigo,tempo,2001110000.0000,2001010000.0000, latitude, 34.0700,34.0700, longitude, 40.3000,40.3000);'




----------------------



savimec 'create_tar("cosmo", "*", "explicit, tempo,dscoor|explicit,latitude,dscoor |explicit,longitude,dscoor", "chuva,double");'



savimec 'load_subtar("cosmo", " total, tempo, 0, 47497001, dstempo |total, latitude, 0 ,47497001, dslatitude| total, longitude, 0, 47497001, dslongitude",  "chuva,dschuvatotal");'





















==================

savimec 'create_tar("oi", "*", "explicit,latitude,dscoortotal |explicit,longitude,dscoortotal", "chuva,double");'

savimec 'load_subtar("oi", " total, latitude, 0 ,10, dslat| total, longitude, 0, 10, dslong",  "chuva,dschuvatotal");'




































savimec 'create_dataset("dscoor3:long", "0:1:47000000:1");'




