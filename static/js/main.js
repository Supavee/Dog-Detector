$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();
    $('#info').hide();
    $('#text1').hide();
    $('#text2').hide();
    $('#text3').hide();

    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview').hide();
                $('#imagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#info').text('');
        $('#text1').text('');
        $('#text2').text('');
        $('#text3').text('');
        $('#result').hide();
        $('#info').hide();
        $('#text1').hide();
        $('#text2').hide();
        $('#text3').hide();
        readURL(this);
    });

    // Predict
    $('#btn-predict').click(function () {
      var form_data = new FormData($('#upload-file')[0]);

      // Show loading animation
      $(this).hide();
      $('.loader').show();
      // $('#head').hide();

      // Make prediction by calling api /predict
      $.ajax({
          type: 'POST',
          url: '/predict',
          data: form_data,
          contentType: false,
          cache: false,
          processData: false,
          async: true,
          success: function (data) {
              // Get and display the result
              $('.loader').hide();
              $('#result').fadeIn(600);
              $('#info').fadeIn(600);
              $('#text1').fadeIn(600);
              $('#text2').fadeIn(600);
              $('#text3').fadeIn(600);

              // $("h2").hide();
              var classes = ['Not Found','Dougie', 'Finn', 'Hana', 'KaoJao', 'Kiara', 'Luke', 'Manny', 'Maple', 'Maya', 'Ninja', 'Topi',];
              var text1="",text2="",text3 = "";
              
              for (i = 0; i < classes.length; i++) {
                if(data==classes[i]) {
                    if(data=='Not Found') {

                        $('#result').text(`Model Predict the Dog as:  ${data}`);
                    }
                    else {
                        $('#result').text(`Model Predict the Dog as:  ${data}`);
                        console.log('yes!');
                        text1 += myObj.INFORMATION[i].USERNAME;
                        text2 += myObj.INFORMATION[i].TEL;
                        text3 += myObj.INFORMATION[i].ADDRESS;
                        $('#result').text(`Model Predict the Dog as:  ${data}`);
                        $('#info').text("User Information");
                        $('#text1').text(" ‍  ‍ - User Name ‍ : "+text1);
                        $('#text2').text(" ‍  ‍ - Tel. ‍  ‍  ‍  ‍   ‍  ‍  ‍  ‍  ‍  ‍  ‍  ‍   ‍      ‍ : "+text2);
                        $('#text3').text(" ‍  ‍ - Address ‍  ‍  ‍  ‍  ‍ ‍  : "+text3);
                        break;
                    }
                  }
              }
            
              console.log('Success!');
          },
      });
    });
});

var myObj;
myObj = { "INFORMATION": [
    {
      "USERNAME": "",
      "TEL": "",
      "ADDRESS": ""
    },
    
    {
      "USERNAME": "John",
      "TEL": "0971530463",
      "ADDRESS": "5/75-6 Soi Samarnmitr New Rd Bang Korlaem Bangkholeam 10120, Bangkok, Thailand"
    },
    {
      "USERNAME": "Jim",
      "TEL": "023456981",
      "ADDRESS": "Charoen Krung 32 Rd.Si Phra Ya Bangrak,Bangkok,10500,Thailand"
    },
    {
      "USERNAME": "Jam",
      "TEL": "0964626636",
      "ADDRESS": "L House, 110 Soi Lat Phrao 8 Yaek 9, Chom Phon,Chatuchak, Bangkok 10900, Thailand"
    },
    {
      "USERNAME": "Jay",
      "TEL": "0863459871",
      "ADDRESS": "/30 Moo.1 Soi.Rama 2(25) T.BangmodA.chom Thong, Bangkok, 10150, Thailand"
    },
    {
      "USERNAME": "Jew",
      "TEL": "025898418",
      "ADDRESS153": "153 4Th Floor The Peninsula Plaza Bluilding Ratchadamri Road Lumpini,\nA.chom Thong, Bangkok, 10330, Thailand"
    },
    {
      "USERNAME": "Jai",
      "TEL": "0642369872",
      "ADDRESS": "1/15 Moo 4 Soi Wong Duan Changwattana Rd.,Bangkok, 10330, Thailand "
    },
    {
      "USERNAME": "Jack",
      "TEL": "0641235987",
      "ADDRESS": "69/55 SOI BANGKADEE 8 Rama Ii Rd. Bangkadee,Bangkok, 10150, Thailand"
    },
    {
      "USERNAME": "Jane",
      "TEL": "0896354781",
      "ADDRESS22": "/5 Gp 5 Chimplee Chimplee Taling Chan,Bangkok, 10170, Thailand"
    },
    {
      "USERNAME": "Jin",
      "TEL": "0975624310",
      "ADDRESS": "63 Ratchadaphisek Soi 18 Ratchadaphisek Road Huai Khwang,Bangkok, 10310, Thailand"
    },
    {
      "USERNAME": "Jo",
      "TEL": "0862459732",
      "ADDRESS": "35/119 Soi Maneeya Village Ramintra Klong Goom Buengkhum,Bangkok, 10230, Thailand"
    },
    {
      "USERNAME": "Jun",
      "TEL": "0612358941",
      "ADDRESS": "Theparak Rd. Muang Samutprakarn Samutprakarn,Bangkok, 10270, Thailand"
    }
  ]
}

// Script to open and close sidebar
function w3_open() {
  document.getElementById("mySidebar").style.display = "block";
  document.getElementById("myOverlay").style.display = "block";
  console.log('open!');
}

function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
  document.getElementById("myOverlay").style.display = "none";
  console.log('close');
}
// Modal Image Gallery
function onClick(element) {
  document.getElementById("img01").src = element.src;
  document.getElementById("modal01").style.display = "block";
  var captionText = document.getElementById("caption");
  var inf1="", inf2="", inf3="";
  var classes = ['Not Found','Dougie', 'Finn', 'Hana', 'Kaojao', 'Kiara', 'Luke', 'Manny', 'Maple', 'Maya', 'Ninja', 'Topi',];   
  captionText.innerHTML = element.alt;         
  for (i = 0; i < classes.length; i++) {
    if(captionText.innerHTML==classes[i]) {
        if(element.alt=='Not Found') {
          console.log('Hi!');
        }
        else {
          inf1 += myObj.INFORMATION[i].USERNAME;
          inf2 += myObj.INFORMATION[i].TEL;
          inf3 += myObj.INFORMATION[i].ADDRESS;
          console.log('test');
        }
      }
  }
  $('#inf1').text("Dog Owner :"+inf1);
  $('#inf2').text("Tel. "+inf2);
  $('#inf3').text("Address :"+inf3);
  console.log('onclick');
}