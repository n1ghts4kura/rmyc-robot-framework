# rm_define.py
# 占位符：用于linting补全，真实值请在运行环境提供

# 装甲板检测
cond_ir_hit_detection = "cond_ir_hit_detection"

# 传感器转接板条件事件（示例与模板）
cond_sensor_adapter1_port2_high_event = "cond_sensor_adapter1_port2_high_event"
cond_sensor_adapter1_port2_trigger_event = "cond_sensor_adapter1_port2_trigger_event"
# 模板占位符，真实环境中会按板号/端口/判断类型展开
cond_sensor_adapter_port_event_template = "cond_sensor_adapter[board_id]_port[port_id]_[judge_type]_event"
cond_sensor_adapter_board_port_judge_event = "cond_sensor_adapter[board_id]_port[port_id]_[judge_type]_event"

# 视觉标记颜色枚举
marker_detection_color_red = "marker_detection_color_red"
marker_detection_color_green = "marker_detection_color_green"
marker_detection_color_blue = "marker_detection_color_blue"

# 红外测距条件占位
cond_ir_distance_template = "ir_distance_[port_id]_[compare_type]_[dist]"
cond_ir_distance1_gt_50 = "ir_distance_1_gt_50"

# 音频枚举
media_sound_recognize_success = "media_sound_recognize_success"
media_sound_solmization_1A = "media_sound_solmization_1A"
