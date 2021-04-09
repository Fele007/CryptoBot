import broker_api, request
from request import Request, Order

if __name__ == "__main__":
    api = broker_api.Binance()
    buy_request = Order("BTCEUR", 1, 40000)
    buy_request.sign(api)
    print(buy_request.query_string)










"""def rawurlencode: 
    local value="$1"
    local len=${#value}
    local encoded=""
    local pos c o

    for (( pos=0 ; pos<len ; pos++ ))
    do
        c=${value:$pos:1}
        case "$c" in
            [-_.~a-zA-Z0-9] ) o="${c}" ;;
            * )   printf -v o '%%%02x' "'$c"
        esac
        encoded+="$o"
    done

    echo "$encoded"
}

ts=$(date +%s000)
paramsWithTs="$apiParams&timestamp=$ts"

rawSignature=$(echo -n "$paramsWithTs" \
               | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem \
               | openssl enc -base64 \
               | tr -d '\n')
signature=$(rawurlencode "$rawSignature")

curl --silent -H "X-MBX-APIKEY: $apiKey" \
     -X $apiMethod "https://testnet.binance.vision/api/$apiCall?$paramsWithTs&signature=$signature"

"""