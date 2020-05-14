let baggage_number = 0;

let form;
let layer;

fn_baggage_add = function () {
    baggage_number += 1;
    let html = '' +
        '<div class="layui-form-item" id="baggage_' + baggage_number + '">\n' +
        '            <div class="layui-inline">\n' +
        '                <label class="layui-form-label">尺寸</label>\n' +
        '                <div class="layui-input-inline" style="width: 100px;">\n' +
        '                    <input type="text" name="length" placeholder="长" autocomplete="off" class="layui-input">\n' +
        '                </div>\n' +
        '                <div class="layui-form-mid">-</div>\n' +
        '                <div class="layui-input-inline" style="width: 100px;">\n' +
        '                    <input type="text" name="width" placeholder="宽" autocomplete="off" class="layui-input">\n' +
        '                </div>\n' +
        '                <div class="layui-form-mid">-</div>\n' +
        '                <div class="layui-input-inline" style="width: 100px;">\n' +
        '                    <input type="text" name="height" placeholder="高" autocomplete="off" class="layui-input">\n' +
        '                </div>\n' +
        '            </div>\n' +
        '\n' +
        '            <div class="layui-inline">\n' +
        '                <label class="layui-form-label">重量</label>\n' +
        '                <div class="layui-input-inline" style="width: 100px;">\n' +
        '                    <input type="text" name="weight" placeholder="Kg" autocomplete="off" class="layui-input">\n' +
        '                </div>\n' +
        '            </div>\n' +
        '        </div>';
    if (baggage_number === 1)
        $("#operator").after(html);
    else
        $('#baggage_' + (baggage_number - 1)).after(html);
};

fn_baggage_remove = function () {
    if (baggage_number === 0) return;
    $('#baggage_' + baggage_number).remove();
    baggage_number -= 1;
};

fn_area_switch = function () {
    const radio_country = parseInt($("input[name='country']:checked").val());
    if (radio_country === 1) $("#area").hide();
    else if (radio_country === 2) $("#area").show();
};

let fn_form_submit;
$(function () {
    layui.use(['form', 'layer'], function () {
        layer = layui.layer;
    });

    fn_form_submit = function () {
        const radio_country = parseInt($("input[name='country']:checked").val());
        const radio_ship_class = parseInt($("input[name=ship_class]:checked").val());
        const price_ticket = parseInt($("input[name=price_ticket]").val());
        const area = parseInt($("#area option:selected").val());

        let baggage_array = [];
        for (let i = 1; i <= baggage_number; ++i) {
            baggage_array.push({
                "length": parseFloat($("#baggage_" + i + " input[name='length']").val()),
                "width": parseFloat($("#baggage_" + i + " input[name='width']").val()),
                "height": parseFloat($("#baggage_" + i + " input[name='height']").val()),
                "weight": parseFloat($("#baggage_" + i + " input[name='weight']").val()),
            })
        }

        let post_data;
        post_data = {
            "country": radio_country,
            "ship": radio_ship_class,
            "price": price_ticket,
            "baggage": baggage_array,
            "area": area
        };

        layer.alert('输入不合法(不是一个包裹)')
        $.ajax({
            type: 'POST',
            url: '/baggage',
            data: JSON.stringify(post_data),
            success: function (data) {
                // layer.alert('一共需要支付' + data + '人民币');
            },
            contentType: "application/json",
            dataType: 'json'
        });
    };


});

