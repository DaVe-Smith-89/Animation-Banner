
echo
while true; do
    read -p "Do you wan´t to change $ mark( y /n )" yn
    case $yn in
        [Yy]* ) bash a6.sh ; break;;
        [Nn]* ) bash a5.sh ;;
        * ) echo "Please answer   yes    or    no.";;
    esac
done

