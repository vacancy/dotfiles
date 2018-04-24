set +e +x 

export PATH=$HOME/anaconda3/bin:$PATH  # Hack:: manually add the PATH prefix

if [ -d $HOME/anaconda3/envs/pytorch ]
then
    conda env remove --name pytorch
fi

conda env create -f environment.yml

