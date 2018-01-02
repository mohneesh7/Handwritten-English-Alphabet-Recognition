m=0;
fol=dir;
mkdir('Data');
mkdir('Processed');
for i=3:size(fol)
    if(strfind(fol(i).name,'.jpg'))
        m=segmentation(fol(i).name,m);
        fprintf ('%s %d\n',fol(i).name,m);
    end
end
