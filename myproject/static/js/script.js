function togglePassword() {
    const pw = document.getElementById('password');
    pw.type = pw.type === 'password' ? 'text' : 'password';
  }

  
  // home page
  function toggleChat() {
    const chat = document.getElementById("chatWindow");
    chat.style.display = chat.style.display === "flex" ? "none" : "flex";
  }
  
  function openPostModal() {
    document.getElementById("postModal").style.display = "flex";
  }
  
  function closePostModal() {
    document.getElementById("postModal").style.display = "none";
  }
  
  