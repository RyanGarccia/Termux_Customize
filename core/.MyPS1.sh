#!/bin/sh
#
#                     List Colors
#######################################################
G="\033[36m"   W="\033[0;0m"    B="\033[1;94m"
Y="\033[1;93m"   R="\033[1;91m"   C="\033[1;96m"
#######################################################
NickName(){
clear
echo "$G"
figlet -f smslant "       NickName"
echo
echo "   Escolha um NickName de pelo menos 8 caracteres..."
echo "                 Digite seu NikName"
echo
read -p "{Nick}~>> " NICKNAME
sleep 0.5
echo
echo "    Processando seu NickName, Por favor aguarde..."
sleep 3
echo
echo "          Seu NickName é: '$NICKNAME'..."
echo
echo
sleep 3
echo '          Escolha uma "PROMPT DE COMANDO"...'
echo
echo " A) ꧁⃟᎒⃟᭄ <<<~>>>꧁⃟᎒⃟᭄ { $NICKNAME }꧁⃟᎒⃟᭄ <<<~>>>꧁⃟᎒⃟᭄  "
echo
echo " ~ ➢➣➢"
echo
echo " B) { $NICKNAME }~➢➣➢"
echo " C) {TERMUX}~➢➣➢"
echo " D) {><}~>>"
echo " E) localhost@$NICKNAME ~#"
echo " F) termux@$NICKNAME ~#"
echo " G) ~ ➢➣➢"
echo " H) kali@linux ~#"
echo " I) M∆ST£R H∆CKING ~>: "
echo " J) Editor (Faça você mesmo)..."
echo " X) Sair..."
echo "$G"
read -p "{=MyPS1=}~➢➣➢ " ESCOLHA
CHOOSER=$(echo $ESCOLHA | tr a-z A-Z)
case $CHOOSER in

A)
echo "               Não gostou da prompt?"
echo
echo "    entre no arquivo bashrc e faça sua edição..."
echo
echo
echo "         Aplicando Tema. Por favor aguarde..."
sleep 5
cd
cd ..
cd usr
cd etc
echo "PS1='\n\033[1;92m   ꧁⃟᎒⃟᭄<<<~>>>꧁⃟᎒⃟᭄ {\033[0;0m $NICKNAME \033[1;92m}꧁⃟᎒⃟᭄<<<~>>>꧁⃟᎒⃟᭄\033[0m\n\n\W ➢➣➢ '" >>bash.bashrc
echo "$G                  Aplicado com sucesso"
;;

B)
echo "               Não gostou da prompt?"
echo
echo "    entre no arquivo bashrc e faça sua edição..."
echo
echo
echo "         Aplicando Tema. Por favor aguarde..."
sleep 5
cd
cd ..
cd usr
cd etc
echo "PS1='{ $NICKNAME }~➢➣➢ '" >>bash.bashrc
echo "$G                  Aplicado com sucesso"
;;

C)
echo "               Não gostou da prompt?"
echo
echo "    entre no arquivo bashrc e faça sua edição..."
echo
echo
echo "         Aplicando Tema. Por favor aguarde..."
sleep 5
cd
cd ..
cd usr
cd etc
echo "PS1='{ TERMUX }~➢➣➢ '" >>bash.bashrc
echo "$G                  Aplicado com sucesso"
;;

D)
echo "               Não gostou da prompt?"
echo
echo "    entre no arquivo bashrc e faça sua edição..."
echo
echo
echo "         Aplicando Tema. Por favor aguarde..."
sleep 5
cd
cd ..
cd usr
cd etc
echo "PS1='{><}~>> '" >>bash.bashrc
echo "$G                  Aplicado com sucesso"
;;

E)
echo "               Não gostou da prompt?"
echo
echo "    entre no arquivo bashrc e faça sua edição..."
echo
echo
echo "         Aplicando Tema. Por favor aguarde..."
sleep 5
cd
cd ..
cd usr
cd etc
echo "PS1='localhost@$NICKNAME ~# '" >>bash.bashrc
echo "$G                  Aplicado com sucesso"
;;

F)
echo "               Não gostou da prompt?"
echo
echo "    entre no arquivo bashrc e faça sua edição..."
echo
echo
echo "         Aplicando Tema. Por favor aguarde..."
sleep 5
cd
cd ..
cd usr
cd etc
echo "PS1='termux@$NICKNAME ~# '" >>bash.bashrc
echo "$G                  Aplicado com sucesso"
;;

G)
echo "               Não gostou da prompt?"
echo
echo "    entre no arquivo bashrc e faça sua edição..."
echo
echo
echo "         Aplicando Tema. Por favor aguarde..."
sleep 5
cd
cd ..
cd usr
cd etc
echo "PS1='\W ➢➣➢ '" >>bash.bashrc
echo "$G                  Aplicado com sucesso"
;;

H)
echo "               Não gostou da prompt?"
echo
echo "    entre no arquivo bashrc e faça sua edição..."
echo
echo
echo "         Aplicando Tema. Por favor aguarde..."
sleep 5
cd
cd ..
cd usr
cd etc
echo "PS1='kali@linux ~# '" >>bash.bashrc
echo "$G                  Aplicado com sucesso"
;;

I)
echo "               Não gostou da prompt?"
echo
echo "    entre no arquivo bashrc e faça sua edição..."
echo
echo
echo "         Aplicando Tema. Por favor aguarde..."
sleep 5
cd
cd ..
cd usr
cd etc
echo "PS1='M∆ST£R H∆CKING ~>: '" >>bash.bashrc
echo "$G                  Aplicado com sucesso"
;;

J)
EDITOR(){
clear
echo "$G"
echo "  Nesta opção você mesmo faz a sua prompt de comando"
echo "             do resto eu me encarrego..."
sleep 6
clear
echo "$G"
figlet -f smslant "            Editor"
echo "      Aqui está o editor, faça seu trabalho..."
echo "   Aconselho que faça a sua prompt em outro editor.."
echo "    e depois cole o seu trabalho aqui, pois o READ"
echo "     não permite que você volte algumas 'CASAS' da"
echo "                   linha de comando...."
echo
echo '  Duvidas?, digite "help"...'
echo
read USERCUSTOM
if [ "$USERCUSTOM" = "help" ];then
    clear
    echo         "Aqui estão algumas ferramentas..."
    echo
    echo
    echo "• \s Mostra o nome do shell."
    echo "• \u Nome do usuário que está usando o shell."
    echo "• \h Mostra o nome do  hostname"
    echo "• \w Contém o nome do diretório corrente desde a raiz."
    echo "• \d Mostra a data no formato: Sun Mar 17."
    echo "• \T Mostra a hora atual no formato: 12:18:22."
    echo "• \W Contém somente o nome do diretório corrente."
    echo
    echo " Aperte 'ENTER' para prosseguir..."
    read ENTER
    EDITOR
else
    cd
    cd ..
    cd usr
    cd etc
    echo "      Sua prompt é: $USERCUSTOM"
    sleep 3
    echo "PS1='$USERCUSTOM '" >>bash.bashrc
    sleep 5
    echo "$G                  Aplicado com sucesso"
fi
}
	EDITOR
;;

X)
echo "$G"
echo "            Obrigado por utilizar o script..."
exit
;;

*)
echo "$G"
echo "             Opção inválida, Reiniciando..."
sleep 4
	NickName
;;
esac
}
	NickName
