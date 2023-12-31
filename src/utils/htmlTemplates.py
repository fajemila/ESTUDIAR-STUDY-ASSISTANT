css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #14700a; /* changed this line */
    color: red;
    font-family: Arial, Helvetica, sans-serif;
}
.chat-message.bot {
    background-color: #14700a;
    font-family: Arial, Helvetica, sans-serif;
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 40px;
  max-height: 40px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 60%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 40px; max-width: 40px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png" style="max-height: 40px; max-width: 40px; border-radius: 50%; object-fit: cover;">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
