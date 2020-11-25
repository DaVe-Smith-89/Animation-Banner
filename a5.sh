echo
while true; do
    read -p "Are you wan´t to make banner with animation(y/n)" yn
    case $yn in
        [Yy]* ) bash customa.sh ; break;;
        [Nn]* ) bash cusyom.sh ;;
        * ) echo "Please answer   yes    or    no.";;
    esac
done

