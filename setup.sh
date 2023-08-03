mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
primaryColor = \"#0E8388\"\n\
backgroundColor = \"#2C3333\"\n\
secondaryBackgroundColor = \"#2E4F4F\"\n\
textColor = \"#CBE4DE\"\n\
font = \"monospace\"\n\
" > ~/.streamlit/config.toml
