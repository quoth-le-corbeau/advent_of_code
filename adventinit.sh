#!/bin/bash

echo "A New Year =============================================================================================================================" 
echo "   _____                 __  .__                      _____       .___                    __            _____  _________            .___      
  /  _  \   ____   _____/  |_|  |__   ___________    /  _  \    __| _/__  __ ____   _____/  |_    _____/ ____\ \_   ___ \  ____   __| _/____  
 /  /_\  \ /    \ /  _ \   __\  |  \_/ __ \_  __ \  /  /_\  \  / __ |\  \/ // __ \ /    \   __\  /  _ \   __\  /    \  \/ /  _ \ / __ |/ __ \ 
/    |    \   |  (  <_> )  | |   Y  \  ___/|  | \/ /    |    \/ /_/ | \   /\  ___/|   |  \  |   (  <_> )  |    \     \___(  <_> ) /_/ \  ___/ 
\____|__  /___|  /\____/|__| |___|  /\___  >__|    \____|__  /\____ |  \_/  \___  >___|  /__|    \____/|__|     \______  /\____/\____ |\___  >
        \/     \/                 \/     \/                \/      \/           \/     \/                              \/            \/    \/ "
echo "Let's get this party started ==========================================================================================================="
read -p "Enter the absolute path to your project: [${HOME}/code/advent]" project_path
project_path="${project_path:-$HOME/code/advent}"
echo "project path set to $project_path"
read -p "What year is it?: " project_year

project_dir="${project_path}/advent_${project_year}"
if [ -d "$project_dir" ]; then
  echo "$project_dir already exists!"
  exit 1
else
  mkdir -p $project_dir || { echo "Creating ${project_dir} failed. Sorry!" ; exit 1; }
  echo "successfully created: $project_path"
fi

solution_template=~/.scripts/aoctmpl.py || { echo "Finding ${solution_template} failed. Sorry!" ; exit 1; }

for day_number in $(seq 25 $END); do 
    project_day_dir="${project_dir}/day_${day_number}"
    mkdir -p $project_day_dir || { echo "Creating ${project_day_dir} failed. Sorry!" ; exit 1; };
    cat $solution_template > $project_day_dir/p1.py || { echo "Creating ${project_day_dir}/p1.py failed. Sorry!" ; exit 1; };
    cat $solution_template > $project_day_dir/p2.py || { echo "Creating ${project_day_dir}/p2.py failed. Sorry!" ; exit 1; };
    touch $project_day_dir/eg.txt || { echo "Creating ${project_day_dir}/eg.txt failed. Sorry!" ; exit 1; };
    touch $project_day_dir/input.txt || { echo "Creating ${project_day_dir}/input.txt failed. Sorry!" ; exit 1; };
done

echo "$project_dir successfully created! Happy coding!"
