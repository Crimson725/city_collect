from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, RadioField
from wtforms import SelectField, TextAreaField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    gender = RadioField(
        '您的性别',
        validators=[DataRequired('请选择标签！')],
        choices=[('1', u'男性'), ('2', u'女性')],
        render_kw={
            'class': 'radio_type',
            'type': 'radio',
            'checked': 'checked',
            'required': 'required'
        },
        coerce=int
    )

    age = SelectField(
        label='您的年龄',
        validators=[DataRequired('请选择标签！')],
        render_kw={
            'class': 'radio_type',
            'checked': 'checked',
            'required': 'required'
        },
        choices=[(1, u'未满16岁'), (2, u'16-30岁'), (3, u'30-55岁'), (4, u'55岁以上')],
        default=4,
        coerce=int
    )

    profession = SelectField(
        label='您的职业',
        validators=[DataRequired('请选择标签！')],
        render_kw={
            'class': 'radio_type',
            'checked': 'checked'
        },
        choices=[(1, u'农、林、牧、渔业生产及辅助人员'), (2, u'生产制造及有关人员'), (3, '建筑业及辅助人员'), (4, '金融业及有关人员')
            , (5, '信息传输、软件和信息技术服务业'), (6, '教育、科学研究和技术服务业'), (7, u'水利、环境和公共设施管理业'),
                 (8, u'交通运输、仓储和邮政业'), (9, u'卫生和社会工作及辅助人员'), (10, u'餐饮、住宿、文化、体育和娱乐业'),
                 (11, u'公共管理、社会保障和社会（国际）组织'), (12, u'青年及在校学生'), (13, u'失业、无业或退休人员')],
        default=8,
        coerce=int
    )

    earthquake = StringField('您是否经历过大地震？')
    earthquake_checkbox_1 = BooleanField('经历过512大地震')
    earthquake_checkbox_2 = BooleanField('在震中')
    earthquake_checkbox_3 = BooleanField('在震源附近')
    earthquake_checkbox_4 = BooleanField('未经历过')

    living = RadioField(
        '您曾在都江堰居住过吗？',
        validators=[DataRequired('请选择标签！')],
        choices=[('1', u'从未居住过'), ('2', u'现在在都江堰'), (3, u'曾经居住过')],
        render_kw={
            'class': 'radio_type',
            'type': 'radio',
            'checked': 'checked',
            'required': 'required'
        },
        coerce=int
    )

    travel = RadioField(
        '您曾到都江堰旅游过吗？',
        validators=[DataRequired('请选择标签！')],
        choices=[('1', u'从未到访'), ('2', u'最近五年曾到访'), (3, u'五年之前曾到访')],
        render_kw={
            'class': 'radio_type',
            'type': 'radio',
            'checked': 'checked',
            'required': 'required'
        },
        coerce=int
    )

    feedback = TextAreaField(
        '留下您宝贵的建议.',
        render_kw={
            'class': 'text_area',
            'placeholder': '对调查问卷的意见~\n'
        }
    )

    onclick = "alert('成功')"
    submit = SubmitField('保存并提交', render_kw={'onclick': 'alert("调查问卷已成功提交，感谢您的参与！")'})
