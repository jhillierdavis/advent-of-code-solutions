# Capture current directory location
dir=$PWD
#echo "$dir"

# Loop through sub-directories of each puzzle day & execute unit tests for each
for i in {01..09}; do
    # Pad value (if required) to 2 digits (e.g. 07)
    x=$i
    while [ ${#x} -ne 2 ];
    do
        x="0"$x
    done

    cd $dir/aoc-2025-day-$x
    ./run-tests-solution-in-python3.sh
done
