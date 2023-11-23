from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg  import openapi

from stocks.models import Stock  
from stocks.dto.serializer.stock_serializer import StockSerializer
from stocks.facades.stock_facade import StockFacade

class StockController(viewsets.ViewSet):
    http_method_names = ['get', 'post']
    serializer_class = StockSerializer

    @swagger_auto_schema(
        operation_description="주식 종목 리스트를 조회합니다",
        responses={
            200: openapi.Response(
                description="정상 응답"
            ),
            404: openapi.Response(
                description="주식 종목이 존재하지 않을때"
            ),
            500: openapi.Response(
                description="내부 서버 오류"
            )
        }
    )
    def list(self, request, *args, **kwargs):
        try:
            stocks = StockFacade().GetStockList()
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={})
        print(stocks)
        serializer = StockSerializer(stocks, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    

    @swagger_auto_schema(
        operation_description="주식 종목을 생성합니다",
        request_body=StockSerializer,
        responses={
            200: openapi.Response(
                description="정상 응답"
            ),
            400: openapi.Response(
                description="인자가 정상적이지 않을때"
            ),
            500: openapi.Response(
                description="내부 서버 오류"
            )
        }
    )
    def create(self, request, *args, kwargs):
        data = request.data

        code = data.get('code')
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')
        
        result = StockFacade.CreateStock(code, name, price, description)

        if result is not True:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={})
        
        return Response(status.HTTP_200_OK, data={ "status" : 'created'})