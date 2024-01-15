
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