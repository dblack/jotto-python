git grep -l $1 | xargs ruby -pi -e "gsub(/#{Regexp.escape(\"$1\")}/, '$2')"
