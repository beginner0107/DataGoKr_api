<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>dataList</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
<script src="./js/data.js"></script>
</head>
<body>
<div class="container">
  <div class="table-responsive">
	<h4 style="text-align: center;padding:50px;">JSON 데이터 리스트</h4>
	<table id="member_table" class="table table-striped">
		<thead>
		<tr>
			<th>No</th>
			<th>관할 경찰서</th>
			<th>다발지역 위치</th>
			<th>경상자수</th>
			<th>중상자수</th>
			<th>사망자수</th>
		</tr>
		</thead>
		<tbody>
		</tbody>
	</table>
  </div>
</div>
</body>
</html>