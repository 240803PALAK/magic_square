const gridItems = document.querySelectorAll('.grid-item');
const errorMessage = document.getElementById('error-message');
var xState = [0, 0, 0, 0, 0, 0, 0, 0, 0];
var zState = [0, 0, 0, 0, 0, 0, 0, 0, 0];
let shouldCallHandleGridItemClicks = true;

gridItems.forEach(item => {
  item.addEventListener('click', async function () {
    if (!shouldCallHandleGridItemClicks) {
      return;
    }
    const value = this.dataset.value;
    try {
      const response = await fetch('/play', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          value,
          xState,
          zState
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      xState = data.xState;
      zState = data.zState;
      for (let i = 0; i < data.xState.length; i++) {
        if (data.xState[i] === 1) {
          const item = document.getElementById(`item${i}`);
          item.textContent = "X";
        }
      }
      for (let i = 0; i < data.zState.length; i++) {
        if (data.zState[i] === 1) {
          const item = document.getElementById(`item${i}`);
          item.textContent = "O";
        }
      }
      errorMessage.textContent = data.message;
      if (data.message === "System Won" || data.message === "It's a Draw" || data.message === "You Won") {
        const horizontal = document.getElementById('hdrawline');
        const vertical = document.getElementById('vdrawline');
        const rotation = document.getElementById('vrdrawline');
        console.log(data.win)
        if (data.win === "[0, 1, 2]") {
          vertical.style.display = 'inline-block';
          vertical.style.marginBottom = "335px";  
        }
        if (data.win === "[3, 4, 5]") {
          vertical.style.display = 'inline-block';
          vertical.style.marginBottom = "0px";  
        }
        if (data.win === "[6, 7, 8]") {
          vertical.style.display = 'inline-block';
          vertical.style.marginBottom = "-335px";  
        }

        if (data.win === "[0, 3, 6]") {
          horizontal.style.display = 'inline-block';
          horizontal.style.marginLeft = "-235px";  
        }
        if (data.win === "[1, 4, 7]") {
          horizontal.style.display = 'inline-block';
          horizontal.style.marginLeft = "235px";  
        }
        if (data.win === "[2, 5, 8]") {
          horizontal.style.display = 'inline-block';
          horizontal.style.marginLeft = "715px";  
        }
        if (data.win === "[0, 4, 8]") {
          rotation.style.display = 'inline-block';
          rotation.style.marginBottom='-20px;';
          rotation.style.transform = "rotate(35deg)" 
        }
        if (data.win === "[2, 4, 6]") {
          rotation.style.display = 'inline-block';
          rotation.style.marginBottom='0px;';
          rotation.style.transform = "rotate(-35deg)"
        }
        shouldCallHandleGridItemClicks = false;
      }
    } catch (error) {
      console.error('Error:', error);
    }

  });
})






