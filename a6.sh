echo
while true; do
    read -p "Do you wan´t to make banner with animation:( y /n )" yn
    case $yn in
        [Yy]* ) bash customam.sh ; break;;
        [Nn]* ) bash customm.sh ;;
        * ) echo "Please answer   yes    or    no.";;
    esac
done

