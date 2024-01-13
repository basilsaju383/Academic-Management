
    function delete_row(row){
        
        var box = $("#mb-remove-row");
        box.addClass("open");
        
        box.find(".mb-control-yes").on("click",function(){
            box.removeClass("open");
            $("#"+row).hide("slow",function(){
                $(this).remove();
            });
        });
        
    }
    function poping(id) {
       
        alert('fff')
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
                url: div_url,
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

    
    

   