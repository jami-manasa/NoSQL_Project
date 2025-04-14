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

  

  // post home page next page 

  document.addEventListener("DOMContentLoaded", () => {
    const postsPerPage = 2;
    let currentPage = 1;

    const posts = document.querySelectorAll(".post-card");
    const totalPages = Math.ceil(posts.length / postsPerPage);

    function showPosts(page) {
      const start = (page - 1) * postsPerPage;
      const end = start + postsPerPage;

      posts.forEach((post, index) => {
        post.style.display = (index >= start && index < end) ? "block" : "none";
      });

      document.getElementById("pageNumber").textContent = `Page ${page}`;
      document.getElementById("prevPage").disabled = page === 1;
      document.getElementById("nextPage").disabled = page === totalPages;
    }

    // Initial load
    showPosts(currentPage);

    // Pagination buttons
    document.getElementById("prevPage").addEventListener("click", () => {
      if (currentPage > 1) {
        currentPage--;
        showPosts(currentPage);
      }
    });

    document.getElementById("nextPage").addEventListener("click", () => {
      if (currentPage < totalPages) {
        currentPage++;
        showPosts(currentPage);
      }
    });
  });
  