set +e +x 

export PATH=$HOME/anaconda3/bin:$PATH  # Hack:: manually add the PATH prefix

conda create --name pytorch
source activate pytorch
conda install torchvision pytorch -c pytorch
