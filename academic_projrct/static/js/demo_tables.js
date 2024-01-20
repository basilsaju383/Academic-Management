
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


    function sub_lists(id) {
        var subjectDropdown = document.getElementById("subjectDropdown");
        document.getElementById("subjectDropdown").innerHTML="";
        $.ajax({
            url: "/sub_listss/",
            type: 'GET',
            data: { "classId": id },
            dataType: 'json',
            success: function (data) {
                // Clear existing options
                subjectDropdown.innerHTML = "";
        
                // Check if data.subjects is defined and not empty
                if (data.subjects && data.subjects.length > 0) {
                    // Create default option
                    var defaultOption = document.createElement("option");
                    defaultOption.value = 0;
                    defaultOption.text = "--select subject--";
                    subjectDropdown.add(defaultOption);
        
                    // Add options based on data.subjects
                    data.subjects.forEach(function (item) {
                        var option = document.createElement("option");
                        option.value = item.id || '';  
                        option.text = item.sub_name;
                        subjectDropdown.add(option);
                    });
                } else {
                    // If no subjects, display a message or handle it as needed
                    console.log('No subjects available');
                }
            },
            
            error: function (error) {
                console.log('Error fetching subjects:', error);
            }
        });
    }
    

    function subclass_adding() {
    var select_class = $('#sel_cls option:selected').text();
    var select_division = $('#div_select option:selected').text();
    var select_subject = $('#subjectDropdown option:selected').text();
    var selected_classid = $('#sel_cls').val();
    var selected_divid = $('#div_select').val();
    var selected_subid = $('#subjectDropdown').val();

    if ($('#sel_cls')[0].selectedIndex === 0 || $('#div_select')[0].selectedIndex === 0 || $('#subjectDropdown')[0].selectedIndex === 0) 
    {
        alert('Please select a class , Division and Subject.');
        return;
    }

    

    // Check if the combination already in the table
    var combinationExists = false;

    $('#tabledata tr').each(function () {
        var existingClass = $(this).find('td:eq(1)').text().trim();
        var existingDivision = $(this).find('td:eq(2)').text().trim();
        var existingSubject = $(this).find('td:eq(3)').text().trim();

        if (
            existingClass === select_class &&
            existingDivision === select_division &&
            existingSubject === select_subject
        ) {
            combinationExists = true;
            return false; // Break out of the loop if a matching row is found
        }
    });

    // If the row does not exist, append a new one
    if (combinationExists) {
        alert('Combination already exists.');
    } else {
        var serial=0;

        serial++;
        var newRow =
            '<tr>' +
            '<td>' + serial + '</td>' +
            '<td>' + select_class + '<input type="hidden" value="'+selected_classid+'" name="selcls"></td>' +
            '<td>' + select_division + '<input type="hidden" value="'+selected_divid+'" name="seldiv"></td>' +
            '<td>' + select_subject + '<input type="hidden" value="'+selected_subid+'" name="selsub"></td>' +
            '<td><button class="deleteRow btn-danger">Remove</button></td>' +
            '</tr>';

        $('#tabledata').append(newRow);
        document.getElementById('sel_cls').value='';
        document.getElementById('div_select').value='';
        document.getElementById('subjectDropdown').innerHTML='<option value="">Select Subject</option>';
    }

    // delete row functionality
    $('#tabledata').on('click', '.deleteRow', function () {
        // serial--; // Decrement serial when deleting a row
        $(this).closest('tr').remove();
    });
}