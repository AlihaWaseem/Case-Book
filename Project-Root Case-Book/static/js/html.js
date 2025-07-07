 // html.js — frontend logic for Social Nest

document.addEventListener("DOMContentLoaded", function () {
  // --- DARK MODE TOGGLE ---
  const darkbtn = document.getElementById("dark-btn");
  if (darkbtn) {
    darkbtn.onclick = function () {
      darkbtn.classList.toggle("dark-btn-on");
      document.body.classList.toggle("dark-theme");
      localStorage.setItem("theme", document.body.classList.contains("dark-theme") ? "dark" : "light");
    };
  }

  // Load saved theme
  if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-theme");
    darkbtn?.classList.add("dark-btn-on");
  }

  // --- DROPDOWN MENU TOGGLE ---
  window.settingmenuToggle = function () {
    document.querySelector(".setting-menu")?.classList.toggle("setting-menu-height");
  };

  // --- FETCH AND DISPLAY POSTS ---
  fetch("http://127.0.0.1:5000/api/posts")
    .then((res) => res.json())
    .then((posts) => {
      const mainContent = document.querySelector(".main-content");
      if (!mainContent) return;

      posts.forEach((post) => {
        const postHTML = `
          <div class="post-container">
            <div class="post-row">
              <div class="user-profile">
                <img src="pexel7.jpg" />
                <div>
                  <p>User #${post.user_id}</p>
                  <span>${new Date(post.created_at).toLocaleString()}</span>
                </div>
              </div>
            </div>
            <p class="post-text">${post.content}</p>
            ${post.media_url ? `<img src="${post.media_url}" class="post-img">` : ""}
            <div class="post-row">
              <div class="activity-icon">
                <div><img src="like.png"> 0</div>
                <div><img src="comment.png"> 0</div>
              </div>
            </div>
          </div>
        `;
        mainContent.insertAdjacentHTML("beforeend", postHTML);
      });
    })
    .catch((err) => console.error("Failed to load posts:", err));
});
const navName = document.getElementById("nav-username");
if (navName && localStorage.getItem("username")) {
  navName.textContent = localStorage.getItem("username");
}
