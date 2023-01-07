# Shell script の Tips や備忘録

## Yes/No の選択に応じた対話的実行

- [Answer to: How do I prompt for Yes/No/Cancel input in a Linux shell script?](https://stackoverflow.com/a/226724)

```sh
read -p "Do you wish to execute some command?" yn
case $yn in
    [Yy]* ) execute some command;;
    [Nn]* ) exit;;
    * ) echo "Please answer yes or no.";;
esac
```

## 複数のファイルに対する繰り返し処理

```sh
array_file=("file_a" "file_b" "file_c")
OBJ=${!#}  # Last argument

cd "$(dirname "$0")"  # Move to the directory which has this shell script

# Iteration over files to be combined
for file in "${array_file[@]}"; do
    declare -a array_full_path=()
    # Iteration over subdomains (create array of full file path)
    for subdir in ${@:1:($#-1)}; do
        full_path="$subdir/$file"
        array_full_path+=($full_path)
    done
    # Execute cat
    echo "cat ${array_full_path[@]}  > ${OBJ}/$file"
    cat ${array_full_path[@]}  > ${OBJ}/$file
done
```
