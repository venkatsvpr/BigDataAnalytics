
function load_data()
{
  alert("called");
  var file1="";
  var file2="";
  var pick = document.getElementById("pick").value;
  console.log("Value is : " + pick);
  document.getElementById("word-cloud-NY").innerHTML ="";
  document.getElementById("word-cloud-TR").innerHTML ="";

  switch(pick)
  {

      case "facebook":
                      file1="facebook_NY.txt";
                      file2="facebook_TR.txt";                      
                      break;
      case "india":
                      file1="india_NY.txt";
                      file2="india_TR.txt";                      
                      break;
      case "trump":
                      file1="trump_NY.txt";
                      file2="trump_TR.txt";
                      break;
      case "select":
                      file1="NA";
                      file2="NA";
  }


  var width = 400,
  height = 400,
  show_data = 13;

  var leaderscale = d3.scaleLinear().range([20,30]);
  var leaders = [];
  var leaders1 = [];
  var fill = d3.scaleOrdinal(d3.schemeCategory10);

  d3.tsv("./data/" + file1, function(data){

    leaders.push({text: data.Word, size: data.Freq});

    leaderscale.domain([
        d3.min(leaders,function(d) {return d.size;}),
        d3.max(leaders,function(d) {return d.size;})        
      ]);    

    if(leaders.length==show_data)
    {      
        layout = d3.layout.cloud()
      .size([width, height])
      .words(leaders)
      .padding(2)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return leaderscale(d.size); })
      .on("end", draw);
 
    layout.start();  
    }
        
  }); 

  d3.tsv("./data/" + file2, function(data){

    leaders1.push({text: data.Word, size: data.Freq});

    leaderscale.domain([
        d3.min(leaders1,function(d) {return d.size;}),
        d3.max(leaders1,function(d) {return d.size;})        
      ]);    

    if(leaders1.length==show_data)
    {      
        layout = d3.layout.cloud()
      .size([width, height])
      .words(leaders1)
      .padding(2)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return leaderscale(d.size); })
      .on("end", draw1);
 
    layout.start();  
    }
        
  }); 

  function draw(words) {

  d3.select("#word-cloud-NY").append("svg")
      .attr("width", layout.size()[0])
      .attr("height", layout.size()[1])
    .append("g")
      .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
    .selectAll("text")
      .data(words)
    .enter().append("text")
      .style("font-size", function(d) { return d.size + "px"; })
      .style("font-family", "Impact")
      .style("fill", function(d, i) { return fill(i); })
      .attr("text-anchor", "middle")
      .attr("transform", function(d) {
        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
      })
      .text(function(d) { return d.text; });
  }

  function draw1(words) {

  d3.select("#word-cloud-TR").append("svg")
      .attr("width", layout.size()[0])
      .attr("height", layout.size()[1])
    .append("g")
      .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
    .selectAll("text")
      .data(words)
    .enter().append("text")
      .style("font-size", function(d) { return d.size + "px"; })
      .style("font-family", "Impact")
      .style("fill", function(d, i) { return fill(i); })
      .attr("text-anchor", "middle")
      .attr("transform", function(d) {
        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
      })
      .text(function(d) { return d.text; });
  }

}