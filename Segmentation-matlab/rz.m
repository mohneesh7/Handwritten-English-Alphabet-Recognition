function op=rz(letter_imgn,fname)
imagen=imread(['Data\',letter_imgn]);
[i,j,k] = size(imagen);
if i >= j
    diff = i - j;
    d = uint32(diff / 2);
    for p = 1 : i
        for q = 1 : d
            x(p,q,1) = uint8(0);
        end
        for q = 1 : j
            x(p,d+q,1) = imagen(p,q,1);
        end
        for l = 1 : d
            x(p, j+d+l, 1) = uint8(0);
        end
    end
end

if j > i
    diff = j - i;
    d = uint32(diff / 2);
    for p = 1 : d
        for q = 1 : j
            x(p,q,1) = uint8(0);
        end
    end
    for p = 1 : i
        for q = 1 : j
            x(p+d,q,1) = imagen(p,q,1);
        end
    end
    for p = 1 : d
        for q = 1 : j
            x(d+p+i, j, 1) = uint8(0);
        end
    end
end
y = imresize(x,[34 34]);
letter_name = [fname,'\',letter_imgn];
imwrite(y,letter_name,'jpg');