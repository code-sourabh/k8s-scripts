while [[ $# -gt 1 ]]
do
key="$1"

case $key in
    -u|--url)
    target_url="$2"
    shift # past argument
    ;;
    *)
        # unknown option
    ;;
esac
shift # past argument or value
done

format="----------------------------
     time_namelookup:  %{time_namelookup}\n
        time_connect:  %{time_connect}\n
     time_appconnect:  %{time_appconnect}\n
    time_pretransfer:  %{time_pretransfer}\n
       time_redirect:  %{time_redirect}\n
  time_starttransfer:  %{time_starttransfer}\n
----------------------------
         time_total:  %{time_total}\n"

if [ "$target_url" ]; then
  echo "Sending GET request to $target_url"
  curl -w "$format" -o /dev/null -s "$target_url"
else
  echo "Target URL not specified."
fi