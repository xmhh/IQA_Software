function NRQ=NJQA(imagename)
% Example
% imagename = ['log_seaside.JPEG.5' '.png'];
% OUT=NJQA(imagename)
bll=8;
xxx=[];
xxxz=[];
load('img.mat')
dst_img=img;
nz=[];
nz_zaeef=[];
% img=rgb2gray(dst_img);
img=double(img);
[X1 Y1]=size(img);
LEN = 50;
THETA = 5;
PSF = fspecial('motion', LEN, THETA);
blurred = imfilter(img, PSF, 'conv', 'circular');
im_b=blurred;
[im1 im2 im3 ]=s3_map(im_b);
 Map=im1; Map1=Map;
for r=1:bll:X1
    for c=1:bll:Y1
        if r+bll-1> X1
        elseif c+bll-1> Y1
        else
            blk=Map(r:r+bll-1,c:c+bll-1);
            a1=((sum(blk(:))));
            if a1< 0.5
                Map1(r:r+bll-1,c:c+bll-1)=255;
            else
                Map1(r:r+bll-1,c:c+bll-1)=0;
            end
        end
    end
end
for r=1:X1
    for c=1:Y1
        if Map1(r,c)==255
            Map1(r,c)=0;
        else
            Map1(r,c)=255;
        end
    end
end
d=img;
for r=1:bll:X1
    for c=1:bll:Y1
        if r+bll-1> X1
        elseif c+bll-1> Y1
        else
            blk=d(r:r+bll-1,c:c+bll-1);
            a1=((dct2(blk)));
            nn=64-(nnz(a1));
            T3=Map1(r:r+bll-1,c:c+bll-1);
            if mean2(T3)==255 % yani texture dare
                nz_zaeef= [nz_zaeef; nn];
            else % black area
                nz= [nz; nn];
                
            end
            
        end
    end
end
OUT=d;
clc
save_nz=nz;
[N1 N2]=size(nz);
[Nz1 Nz2]=size(nz_zaeef);
for i=1:N1
    if nz(i,1)<=0
        nz(i,1)=0;
    end
end
for i=1:Nz1
    if nz_zaeef(i,1)<=0
        nz_zaeef(i,1)=0;
    end
end
SSI=X1*Y1;
snz=sum(nz(:))/SSI;
snzaeef=sum(nz_zaeef(:))/SSI;
xxx=snz;
xxxz=snzaeef;
NRQ=0.2*xxx+xxxz;
