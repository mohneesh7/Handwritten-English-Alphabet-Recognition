function m=segmentation(imgn,m)
%imgn=uigetfile('*.jpg;*.png;*.gif;*.tif');
imagen=imread(imgn);
Destin_path='Data';
Resized_path='Processed';
%% Convert to gray scale
if size(imagen,3)==3 % RGB image
    imagen=rgb2gray(imagen);
end
%% Convert to binary image
threshold = graythresh(imagen);
imagen =~imbinarize(imagen,threshold);
%% Remove all object containing fewer than 30 pixels
imagen = bwareaopen(imagen,30);
%% Label connected components
[L, Ne]=bwlabel(imagen);
%% Objects extraction
for n=1:Ne
    [r,c] = find(L==n);
    if (min(r)<4 || min(c)<4)
        %%subImage = L(min(r):max(r),min(c):max(c));
        %%filename = [Destin_path,'\',num2str(2000+n),'.jpg'];
        %%imwrite(subImage,filename,'jpg');
        continue;
    else
        up=min(r);
        subImage = L(up:max(r),min(c):max(c));
        while(subImage(1,:)==zeros)
            subImage = L(up:max(r),min(c):max(c));
            up=up-1;
        end
        down=max(r);
        while(subImage(down+1-up,:)==zeros)
            subImage = L(up:down,min(c):max(c));
            down=down+1;
        end
        left=min(c);
        while(subImage(:,1)==zeros)
            subImage = L(up:down,left:max(c));
            left=left-1;
        end
        right=max(c);
        while(subImage(:,right+1-left)==zeros)
            subImage = L(up:down,left:right);
            right=right+1;
        end
        filename = [Destin_path,'\',num2str(0+m),'.jpg'];
        m=m+1;
        imwrite(subImage,filename,'jpg');
    end
end
folder=dir(Destin_path);
for i=3:size(folder)
    rz(folder(i).name,Resized_path);
end
