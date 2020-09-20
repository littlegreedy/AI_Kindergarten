<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

    <title>ECharts 实例</title>
    <!-- 引入 echarts.js -->
    <script src="https://cdn.staticfile.org/echarts/4.3.0/echarts.min.js"></script>
    <script src="https://cdn.bootcss.com/jquery/2.2.4/jquery.js"></script>
    <!-- 引入主题 -->
    <!-- <script src="https://www.runoob.com/static/js/wonderland.js"></script> -->
    <!-- <script src="charts.js"></script> -->
    <style type="text/css">
        div{
            float: right;
            background:	#787878;
        }
    </style>

</head>
<body>
<!-- 为ECharts准备一个具备大小（宽高）的Dom -->
<div id="main" style="width: 1480px;height:750px;"></div>
<!-- <div id="main2" float: right ; style="width: 600px;height:400px;"></div> -->

<script type="text/javascript">
    $.ajax({
        type : "post",
        async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
        url : "studentServlet?method=StudentListJSON",    //请求发送到TestServlet处
        data : {},
        dataType : "json",        //返回数据形式为json
        success : function(result) {
            var builderJson =result;


            var downloadJson = result;

            var themeJson = result;

            var waterMarkText = 'ECHARTS';

            var canvas = document.createElement('canvas');
            var ctx = canvas.getContext('2d');
            canvas.width = canvas.height = 100;
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.globalAlpha = 0.08;
            ctx.font = '20px Microsoft Yahei';
            ctx.translate(50, 50);
            ctx.rotate(-Math.PI / 4);
            ctx.fillText(waterMarkText, 0, 0);


            option = {
                backgroundColor: {
                    type: 'pattern',
                    image: canvas,
                    repeat: 'repeat'
                },
                tooltip: {},
                title: [{
                    text: '在线构建',
                    subtext: '总计 ' + builderJson.all,
                    left: '45%',
                    textAlign: 'center'
                }, {
                    text: '各版本下载',
                    subtext: '总计 ' + Object.keys(downloadJson).reduce(function (all, key) {
                        return all + downloadJson[key];
                    }, 0),
                    left: '83%',
                    textAlign: 'center'
                }, {
                    text: '主题下载',
                    subtext: '总计 ' + Object.keys(themeJson).reduce(function (all, key) {
                        return all + themeJson[key];
                    }, 0),
                    left: '83%',
                    top: '50%',
                    textAlign: 'center'
                }],
                grid: [{
                    top: 50,
                    width: '38%',
                    bottom: '45%',
                    left: 500,
                    containLabel: true
                }, {
                    top: '55%',
                    width: '38%',
                    bottom: 0,
                    left: 500,
                    containLabel: true
                }],
                xAxis: [{
                    type: 'value',
                    max: builderJson.all,
                    splitLine: {
                        show: false
                    }
                }, {
                    type: 'value',
                    max: builderJson.all,
                    gridIndex: 1,
                    splitLine: {
                        show: false
                    }
                }],
                yAxis: [{
                    type: 'category',
                    data: Object.keys(builderJson.charts),
                    axisLabel: {
                        interval: 0,
                        rotate: 30
                    },
                    splitLine: {
                        show: false
                    }
                }, {
                    gridIndex: 1,
                    type: 'category',
                    data: Object.keys(builderJson.components),
                    axisLabel: {
                        interval: 0,
                        rotate: 30
                    },
                    splitLine: {
                        show: false
                    }
                }],
                series: [{
                    type: 'bar',
                    stack: 'chart',
                    z: 3,
                    label: {
                        normal: {
                            position: 'right',
                            show: true
                        }
                    },
                    data: Object.keys(builderJson.charts).map(function (key) {
                        return builderJson.charts[key];
                    })
                }, {
                    type: 'bar',
                    stack: 'chart',
                    silent: true,
                    itemStyle: {
                        normal: {
                            color: '#eee'
                        }
                    },
                    data: Object.keys(builderJson.charts).map(function (key) {
                        return builderJson.all - builderJson.charts[key];
                    })
                }, {
                    type: 'bar',
                    stack: 'component',
                    xAxisIndex: 1,
                    yAxisIndex: 1,
                    z: 3,
                    label: {
                        normal: {
                            position: 'right',
                            show: true
                        }
                    },
                    data: Object.keys(builderJson.components).map(function (key) {
                        return builderJson.components[key];
                    })
                }, {
                    type: 'bar',
                    stack: 'component',
                    silent: true,
                    xAxisIndex: 1,
                    yAxisIndex: 1,
                    itemStyle: {
                        normal: {
                            color: '#eee'
                        }
                    },
                    data: Object.keys(builderJson.components).map(function (key) {
                        return builderJson.all - builderJson.components[key];
                    })
                }, {
                    type: 'pie',
                    radius: [0, '30%'],
                    center: ['83%', '25%'],
                    data: Object.keys(downloadJson).map(function (key) {
                        return {
                            name: key.replace('.js', ''),
                            value: downloadJson[key]
                        }
                    })
                },{
                    name: '访问来源',
                    type: 'pie',    // 设置图表类型为饼图
                    radius: [0, '30%'],  // 饼图的半径，外半径为可视区尺寸（容器高宽中较小一项）的 55% 长度。
                    center: ['13%', '75%'],
                    data:[          // 数据数组，name 为数据项名称，value 为数据项值
                        {value:235, name:'视频广告'},
                        {value:274, name:'联盟广告'},
                        {value:310, name:'邮件营销'},
                        {value:335, name:'直接访问'},
                        {value:400, name:'搜索引擎'}
                    ]
                },{
                    type: 'pie',
                    radius: [0, '30%'],
                    center: ['83%', '75%'],
                    data: Object.keys(themeJson).map(function (key) {
                        return {
                            name: key.replace('.js', ''),
                            value: themeJson[key]
                        };
                    })
                }]
            }
            // myChart.setOption({ // 加载数据图表
            //     xAxis: {
            //         data: names
            //     },
            //     series: [{
            //         // 根据名字对应到相应的系列
            //         name: '销量',
            //         data: nums
            //     }]
            // });

            var myChart = echarts.init(document.getElementById('main'), 'dark');
            myChart.setOption(option);
        }

    })

</script>
<%--<script type="text/javascript">--%>






//     var builderJson = {
//     "all": 10887,
//     "charts": {
//         "map": 3237,
//         "lines": 2164,
//         "bar": 7561,
//         "line": 7778,
//         "pie": 7355,
//         "scatter": 2405,
//         "candlestick": 1842,
//         "radar": 2090,
//         "heatmap": 1762,
//         "treemap": 1593,
//         "graph": 2060,
//         "boxplot": 1537,
//         "parallel": 1908,
//         "gauge": 2107,
//         "funnel": 1692,
//         "sankey": 1568
//     },
//     "components": {
//         "geo": 2788,
//         "title": 9575,
//         "legend": 9400,
//         "tooltip": 9466,
//         "grid": 9266,
//         "markPoint": 3419,
//         "markLine": 2984,
//         "timeline": 2739,
//         "dataZoom": 2744,
//         "visualMap": 2466,
//         "toolbox": 3034,
//         "polar": 1945
//     },
//     "ie": 9743
// };

// var downloadJson = {
//     "echarts.min.js": 17365,
//     "echarts.simple.min.js": 4079,
//     "echarts.common.min.js": 6929,
//     "echarts.js": 14890
// };
//
// var themeJson = {
//     "dark.js": 1594,
//     "infographic.js": 925,
//     "shine.js": 1608,
//     "roma.js": 721,
//     "macarons.js": 2179,
//     "vintage.js": 1982
// };
//
// var waterMarkText = 'ECHARTS';
//
// var canvas = document.createElement('canvas');
// var ctx = canvas.getContext('2d');
// canvas.width = canvas.height = 100;
// ctx.textAlign = 'center';
// ctx.textBaseline = 'middle';
// ctx.globalAlpha = 0.08;
// ctx.font = '20px Microsoft Yahei';
// ctx.translate(50, 50);
// ctx.rotate(-Math.PI / 4);
// ctx.fillText(waterMarkText, 0, 0);
//
//
// option = {
//     backgroundColor: {
//         type: 'pattern',
//         image: canvas,
//         repeat: 'repeat'
//     },
//     tooltip: {},
//     title: [{
//         text: '在线构建',
//         subtext: '总计 ' + builderJson.all,
//         left: '45%',
//         textAlign: 'center'
//     }, {
//         text: '各版本下载',
//         subtext: '总计 ' + Object.keys(downloadJson).reduce(function (all, key) {
//             return all + downloadJson[key];
//         }, 0),
//         left: '83%',
//         textAlign: 'center'
//     }, {
//         text: '主题下载',
//         subtext: '总计 ' + Object.keys(themeJson).reduce(function (all, key) {
//             return all + themeJson[key];
//         }, 0),
//         left: '83%',
//         top: '50%',
//         textAlign: 'center'
//     }],
//     grid: [{
//         top: 50,
//         width: '38%',
//         bottom: '45%',
//         left: 500,
//         containLabel: true
//     }, {
//         top: '55%',
//         width: '38%',
//         bottom: 0,
//         left: 500,
//         containLabel: true
//     }],
//     xAxis: [{
//         type: 'value',
//         max: builderJson.all,
//         splitLine: {
//             show: false
//         }
//     }, {
//         type: 'value',
//         max: builderJson.all,
//         gridIndex: 1,
//         splitLine: {
//             show: false
//         }
//     }],
//     yAxis: [{
//         type: 'category',
//         data: Object.keys(builderJson.charts),
//         axisLabel: {
//             interval: 0,
//             rotate: 30
//         },
//         splitLine: {
//             show: false
//         }
//     }, {
//         gridIndex: 1,
//         type: 'category',
//         data: Object.keys(builderJson.components),
//         axisLabel: {
//             interval: 0,
//             rotate: 30
//         },
//         splitLine: {
//             show: false
//         }
//     }],
//     series: [{
//         type: 'bar',
//         stack: 'chart',
//         z: 3,
//         label: {
//             normal: {
//                 position: 'right',
//                 show: true
//             }
//         },
//         data: Object.keys(builderJson.charts).map(function (key) {
//             return builderJson.charts[key];
//         })
//     }, {
//         type: 'bar',
//         stack: 'chart',
//         silent: true,
//         itemStyle: {
//             normal: {
//                 color: '#eee'
//             }
//         },
//         data: Object.keys(builderJson.charts).map(function (key) {
//             return builderJson.all - builderJson.charts[key];
//         })
//     }, {
//         type: 'bar',
//         stack: 'component',
//         xAxisIndex: 1,
//         yAxisIndex: 1,
//         z: 3,
//         label: {
//             normal: {
//                 position: 'right',
//                 show: true
//             }
//         },
//         data: Object.keys(builderJson.components).map(function (key) {
//             return builderJson.components[key];
//         })
//     }, {
//         type: 'bar',
//         stack: 'component',
//         silent: true,
//         xAxisIndex: 1,
//         yAxisIndex: 1,
//         itemStyle: {
//             normal: {
//                 color: '#eee'
//             }
//         },
//         data: Object.keys(builderJson.components).map(function (key) {
//             return builderJson.all - builderJson.components[key];
//         })
//     }, {
//         type: 'pie',
//         radius: [0, '30%'],
//         center: ['83%', '25%'],
//         data: Object.keys(downloadJson).map(function (key) {
//             return {
//                 name: key.replace('.js', ''),
//                 value: downloadJson[key]
//             }
//         })
//     },{
//         name: '访问来源',
//         type: 'pie',    // 设置图表类型为饼图
//         radius: [0, '30%'],  // 饼图的半径，外半径为可视区尺寸（容器高宽中较小一项）的 55% 长度。
//         center: ['13%', '75%'],
//         data:[          // 数据数组，name 为数据项名称，value 为数据项值
//             {value:235, name:'视频广告'},
//             {value:274, name:'联盟广告'},
//             {value:310, name:'邮件营销'},
//             {value:335, name:'直接访问'},
//             {value:400, name:'搜索引擎'}
//         ]
//     },{
//         type: 'pie',
//         radius: [0, '30%'],
//         center: ['83%', '75%'],
//         data: Object.keys(themeJson).map(function (key) {
//             return {
//                 name: key.replace('.js', ''),
//                 value: themeJson[key]
//             };
//         })
//     }]
// };
//
// var myChart3 = echarts.init(document.getElementById('main'), 'dark');
// myChart3.setOption(option);

<%--</script>--%>
</body>
</html>