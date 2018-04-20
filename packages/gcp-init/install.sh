sudo apt-get install nvidia-384-dev

cd ~

CONDAFILE="Anaconda3-5.1.0-Linux-x86_64.sh"
wget https://repo.continuum.io/archive/$CONDAFILE
bash $CONDAFILE -b
rm $CONDAFILE
echo "export PATH=$HOME/anaconda3/bin:$PATH" >> ~/.config/local_envs

source ~/.zshrc

conda create --name pytorch
source activate pytorch
conda install torchvision pytorch -c pytorch

