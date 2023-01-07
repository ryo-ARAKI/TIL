# Yes/No の選択に応じた対話的実行

- [Answer to: How do I prompt for Yes/No/Cancel input in a Linux shell script?](https://stackoverflow.com/a/226724)

```sh
read -p "Do you wish to execute some command?" yn
case $yn in
    [Yy]* ) execute some command;;
    [Nn]* ) exit;;
    * ) echo "Please answer yes or no.";;
esac
```
