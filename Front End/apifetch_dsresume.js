const countEl = document.getElementById('vc');

updateVisitCount();
//Testinglllll
function updateVisitCount() {
    fetch('https://1nydmobav4.execute-api.us-east-1.amazonaws.com/Prod/visitor_count')
        .then(response => {
        return response.json()
      })
        .then(data => {
            console.log(data)
            document.getElementById('count').innerHTML = data;
        })
    }
