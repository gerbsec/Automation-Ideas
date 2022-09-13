echo "Tool Install Script for Raymond James"
sleep 2
echo "This script takes no arguments and is very safe so run it wtih sudo"
sleep 2
echo "I added that last part for jack, fuck you jack"
sleep 2
echo "Read through it if you don't believe me"
sleep 2
echo "Anyways, sit back relax and enjoy the ride"
sleep 5

echo "Starting full update and upgrade- this will take the longest"
umask 022

sudo apt update && sudo apt dist-upgrade -y

wget https://github.com/syvaidya/openstego/releases/download/openstego-0.8.4/openstego_0.8.4-1_all.deb -O openstego.deb
wget https://github.com/RickdeJager/stegseek/releases/download/v0.6/stegseek_0.6-1.deb -O stegseek.deb

sudo apt install tmux binwalk ruby gem golang zbar-tools tshark checksec build-essential libtool g++ gcc texinfo curl wget automake autoconf python python-dev python3 python3-dev git subversion unzip virtualenvwrapper lsb-release ./openstego.deb ./stegseek.deb tesseract-ocr openjdk-11-jdk stegosuite -y

rm -r openstego.deb stegseek.deb

pip3 install stegoveritas oletools[full] stego-lsb

gem install zsteg

mkdir bin
cd bin

wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
wget https://sourceforge.net/projects/jstego/files/latest/download# -O jstego.jar
wget http://downloads.sourceforge.net/sourceforge/diit/diit-1.5.jar -O diit.jar

chmod +x diit.jar
chmod +x stegsolve.jar
chmod +x jstego.jar

wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.1.5_build/ghidra_10.1.5_PUBLIC_20220726.zip -O ghidra.zip
unzip -n ghidra.zip 

wget https://download.sqlitebrowser.org/DB_Browser_for_SQLite-v3.12.2-x86_64.AppImage -O sqlitebrower.appimage

git clone https://github.com/jesparza/peepdf.git

git clone https://github.com/longld/peda.git ~/peda

wget https://raw.githubusercontent.com/neuroo/apache-scalp/master/scalp.py
wget https://raw.githubusercontent.com/PHPIDS/PHPIDS/master/lib/IDS/default_filter.xml

echo "source ~/peda/peda.py" >> ~/.gdbinit

if [ $(echo "$SHELL") == "/usr/bin/zsh" ];then
        echo "export PATH=/home/sansforensics/bin:\$PATH" >> /home/sansforensics/.zshrc
        echo "alias open='xdg-open'" >> /home/sansforensics/.zshrc
        echo "export PATH=~/.local/bin:\$PATH" >> /home/sansforensics/.zshrc
elif [ $(echo "$SHELL") == "/usr/bin/bash" ];then
        echo "export PATH=/home/sansforensics/bin:\$PATH" >> /home/sansforensics/.bashrc
        echo "alias open='xdg-open'" >> /home/sansforensics/.bashrc
        echo "export PATH=~/.local/bin:\$PATH" >> /home/sansforensics/.bashrc
fi