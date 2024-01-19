
    function delete_row(row,id,urls){
        var box = $("#mb-remove-row");
        box.addClass("open");
        
        box.find(".mb-control-yes").on("click",function(){
            box.removeClass("open");
            $("#"+row).hide("slow",function(){
                $(this).remove();
            });
            
            $.ajax({
                type: "GET",
                url: urls,
                data: {'id': id},
                dataType: "json",
                success: function (data) {
                //$("#mb-delete").modal('show');
                
                },
                error: function (error) {
                    console.log(error);
                }
            });
        });
        
    }
    function poping(id) {
        document.getElementById('divi_id').value=id; 
            $.ajax({
                type: "GET",
                url: "/division_mng_edt/",
                data: {'id': id},
                dataType: "json",
                success: function (data) {
                    document.getElementById('div_name').value=data.name;
                    document.getElementById('div_status').value=data.status;
                    $("#modal_basic").modal('show');
                },
                error: function (error) {
                    console.log(error);
                }
            });
        
      }
      function updt_div() {
        
        var id = document.getElementById('divi_id').value;
        var diviname = document.getElementById('div_name').value;
        var divistatus = document.getElementById('div_status').value;
        var div_url = document.getElementById('divurl').value;
    
            $.ajax({
                type: "GET",
                url:div_url,
                dataType: "json",
                data: { 'id': id, 'diviname': diviname, 'divistatus': divistatus },
                success: function (data) {
                alert(data.message);
                location.reload(true);
            },
            error: function (error) {
                console.log(error);
            }
        });
    }
    

    function dlt_div(id) {
        document.getElementById('divi_id').value=id; 
            $.ajax({
                type: "GET",
                url: "/division_mng_dlt/",
                data: {'id': id},
                dataType: "json",
                success: function (data) {
                $("#mb-delete").modal('show');
                location.reload(true);
                },
                error: function (error) {
                    console.log(error);
                }
            });
        
      }

      function leo(){
        document.getElementById('toggleAll').addEventListener('change',function(){
            var checkboxes = document.getElementsByClassName('icheck');
            for (var i = 0; i < checkboxes.length; i++){
                checkboxes[i].checked = this.checked;
            }
        });
      }

      function atleast(){
        if ($('.icheck:checked').length > 0){
            $('#check').submit();
        }else{
            alert('please select');
            return false
        }
      }

      function sub_view(id) {
        document.getElementById('view').value = id;
        $.ajax({
            type: "GET",
            url: "/subview/",
            data: { 'id': id },
            dataType: "json",
            success: function (data) {
                document.getElementById('viewsubject').innerHTML = data.subname;
                var container = document.getElementById('lists');
                container.innerHTML = '';
                
                // Improved createbox function
                function createbox(id, classname) {
                    var li = document.createElement('li');
                    var span = document.createElement('span');
                    span.id = 'classes';
                    span.innerText = classname;
                    li.appendChild(span);
                    return li;
                }
                data.classes.forEach(function (item) {
                    container.appendChild(createbox(item.id, item.classname));
                });
                $("#modal_basic").modal('show');
            },
            error: function (error) {
                console.log(error);
            }
        });
    }

    
    function showTable(area_id) {
        // Get the selected value from the dropdown
        var selectedOption = document.getElementById("mySelect").value;

        // Get the table element
        var table = document.getElementById("myTable");

        // Check the selected option and show/hide the table accordingly
        if (selectedOption == 1) {
            table.style.display = "table"; // Show the table
        } else {
            table.style.display = "none"; // Hide the table
        }
    }


    function sub_lists() {
       
        var subjectDropdown = document.getElementById("subjectDropdown");
        var classId = document.getElementById("idd").value;
        console.log(classId);
        
        subjectDropdown.innerHTML = '';

        // Fetch subjects based on the selected class using AJAX
        $.ajax({
            url: "/sub_listss/",
            type: 'GET',
            data: { "classId": classId },
            dataType: 'json',
            success: function (data) {
                data.subjects.forEach(function (item) {
                    var option = document.createElement("option");
                    option.value = item.id;
                    option.text = item.sub_name;
                    subjectDropdown.add(option);
                });
            },
            error: function (error) {
                console.log('Error fetching subjects:', error);
            }
        });
    }
    