
function load_data()
{
  //alert("called");
  
  file1="co_facebook_NY.txt";
  file2="co_facebook_TR.txt";

  //console.log("Value is : " + pick);
  document.getElementById("word-cloud-NY").innerHTML ="";
  document.getElementById("word-cloud-TR").innerHTML ="";

 // console.log("line2")

  var width = 400,
  height = 400,
  show_data = document.getElementById("count").value,
  max = 30;


  if(show_data==25)
      var leaderscale = d3.scaleLinear().range([10,15]);

  else if(show_data==20)
    var leaderscale = d3.scaleLinear().range([10,20]);

  else if(show_data==10)
    var leaderscale = d3.scaleLinear().range([15,25]);

  else
     var leaderscale = d3.scaleLinear().range([10,25]);
 
  var leaders = [];
  var leaders1 = [];
  var fill = d3.scaleOrdinal(d3.schemeCategory10);

  d3.tsv("./data/" + file1, function(data){

    leaders.unshift({text: data.Word, size: data.Freq});
    leaderscale.domain([
        d3.min(leaders,function(d) {return d.size;}),
        d3.max(leaders,function(d) {return d.size;})        
      ]);

    if(leaders.length==max)
    {     

      console.log(leaders);

        layout = d3.layout.cloud()
      .size([width, height])
      .words(leaders.slice(0,show_data))
      .padding(2)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return (leaderscale(d.size-(max-show_data))); })
      .on("end", draw);

      layout.start();
    }


  }); 

  d3.tsv("./data/" + file2, function(data){

    leaders1.unshift({text: data.Word, size: data.Freq});

    //console.log(leaders1)

    leaderscale.domain([
        d3.min(leaders1,function(d) {return d.size;}),
        d3.max(leaders1,function(d) {return d.size;})        
      ]);    

    if(leaders1.length==max)
    {      
      console.log(leaders1);
        layout = d3.layout.cloud()
      .size([width, height])
      .words(leaders1.slice(0,show_data))
      .padding(2)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return leaderscale(d.size-(max-show_data)); })
      .on("end", draw1);
 
    layout.start();  
    }
        
  }); 

  function draw(words) {
   // console.log("In draw")

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
  
  //console.log("In draw1")
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