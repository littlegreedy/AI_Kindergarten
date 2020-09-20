package com.lizhou.dao.inter;

import java.util.List;
import java.util.Map;

import com.lizhou.bean.Exam;


/**
 * 操作成绩的数据层接口
 *
 *
 */
public interface ScoreDaoInter extends BaseDaoInter {
	
	/**
	 * 获取学生成绩表
	 * @param exam
	 * @return
	 */
	List<Map<String, Object>> getScoreList(Exam exam);
	
}
