# 複数のファイルに対する繰り返し処理

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
