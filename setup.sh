mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
primaryColor = \"#8DB600\"\n\
backgroundColor = \"#6E7F80\"\n\
secondaryBackgroundColor = \"#A4C639\"\n\
textColor = \"#FFFFFF\"\n\
font = \"sans-serif\"\n\
" > ~/.streamlit/config.toml